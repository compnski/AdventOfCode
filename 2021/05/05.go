package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

const problemNumber = 5

func readInputLines(inputName string) []string {
	data, _ := ioutil.ReadFile(fmt.Sprintf("/Users/jason/src/advent-of-code-2021/%s", inputName))

	lines := strings.Split(string(data), "\n")
	return lines
}

var real = flag.Bool("real", false, "Print real answer")

func main() {
	flag.Parse()

	var testInput = fmt.Sprintf("%02d/test.txt", problemNumber)
	var realInput = fmt.Sprintf("%02d/real.txt", problemNumber)
	_ = realInput
	log.Print("Test: ", solveA(readInputLines(testInput)))
	if *real {
		log.Print("Real: ", solveA(readInputLines(realInput)))
	}

	log.Print("Test: ", solveB(readInputLines(testInput)))
	if *real {
		log.Print("Real: ", solveB(readInputLines(realInput)))
	}
}

type Line struct {
	x1, y1, x2, y2 int
}

func csvToIntArray(data string) (ret []int) {
	splitData := strings.Split(data, ",")
	for _, s := range splitData {
		n, _ := strconv.Atoi(strings.TrimSpace(s))
		ret = append(ret, n)
	}
	return
}

func listCsvToIntArray(data []string) (ret [][]int) {
	for _, s := range data {
		ret = append(ret, csvToIntArray(s))
	}
	return
}

func parseLines(data []string) (ret []Line) {
	for _, lineStr := range data {
		if len(strings.TrimSpace(lineStr)) == 0 {
			continue
		}
		points := listCsvToIntArray(strings.Split(lineStr, "->"))
		ret = append(ret, Line{
			x1: points[0][0],
			y1: points[0][1],
			x2: points[1][0],
			y2: points[1][1],
		})

	}
	return
}

func isStraightLine(line Line) bool {
	return line.x1 == line.x2 || (line.y1 == line.y2)
}

func max(x1, x2 int) int {
	if x1 > x2 {
		return x1
	}
	return x2
}
func min(x1, x2 int) int {
	if x1 > x2 {
		return x2
	}
	return x1
}

func renderLines(lines []Line, straightOnly bool) (board [][]int) {
	var boardSize = 10
	if *real {
		boardSize = 1000
	}

	board = make([][]int, boardSize)
	for i := 0; i < boardSize; i++ {
		board[i] = make([]int, boardSize)
	}
	for _, line := range lines {
		if straightOnly && !isStraightLine(line) {
			continue
		}
		var xStep, yStep = 1, 1
		if line.x1 > line.x2 {
			xStep = -1
		} else if line.x1 == line.x2 {
			xStep = 0
		}
		if line.y1 > line.y2 {
			yStep = -1
		} else if line.y1 == line.y2 {
			yStep = 0
		}
		for x, y := line.x1, line.y1; !(x == (line.x2+xStep) && y == (line.y2+yStep)); x, y = x+xStep, y+yStep {
			board[y][x]++
		}
	}
	return
}

func solveA(data []string) int {
	var dangerArea int
	lines := parseLines(data)
	board := renderLines(lines, true)
	for _, line := range board {
		for _, h := range line {
			if h >= 2 {
				dangerArea++
			}
		}
	}
	return dangerArea
}

func solveB(data []string) int {
	var dangerArea int
	lines := parseLines(data)
	board := renderLines(lines, false)
	for _, line := range board {
		log.Print(line)
		for _, h := range line {
			if h >= 2 {
				dangerArea++
			}
		}
	}
	return dangerArea
}
