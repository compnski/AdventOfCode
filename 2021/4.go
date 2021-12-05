package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

const problemNumber = 4

func readInputLines(inputName string) []string {
	data, _ := ioutil.ReadFile(fmt.Sprintf("/home/jason/src/advent-of-code-2021/%s", inputName))
	lines := strings.Split(string(data), "\n")
	return lines
}

func main() {

	var testInput = fmt.Sprintf("%02d.test.txt", problemNumber)
	var realInput = fmt.Sprintf("%02d.real.txt", problemNumber)
	_ = realInput
	log.Print("Test: ", solveA(readInputLines(testInput)))
	log.Print("Real: ", solveA(readInputLines(realInput)))

	log.Print("Test: ", solveB(readInputLines(testInput)))
	log.Print("Real: ", solveB(readInputLines(realInput)))

}

type Board struct {
	data []int
}

func parseMovesAndBoards(data []string) ([]int, []Board) {
	var moves []int
	for _, n := range strings.Split(data[0], ",") {
		intVal, _ := strconv.Atoi(n)
		moves = append(moves, intVal)
	}

	var boards []Board
	for i := 2; i < len(data); i += 6 {
		var b = Board{data: []int{}}
		for j := 0; j < 5; j++ {
			for _, n := range strings.Split(data[i+j], " ") {
				n = strings.TrimSpace(n)
				if n != "" {
					intVal, _ := strconv.Atoi(n)
					b.data = append(b.data, intVal)
				}
			}
		}
		//		log.Print(b)
		boards = append(boards, b)
	}
	return moves, boards
}

func rowColFromOffset(offset int) (r, c int) {
	return offset / 5, offset % 5
}

func runBingo(moves []int, targetBoard Board) (winningIndex, markedSum int) {
	var (
		countByRow = []int{0, 0, 0, 0, 0}
		countByCol = []int{0, 0, 0, 0, 0}
	)

	for moveNum, move := range moves {
		for idx, n := range targetBoard.data {
			if n == move {
				r, c := rowColFromOffset(idx)
				countByRow[r]++
				countByCol[c]++
				markedSum += n
				if countByRow[r] == 5 || countByCol[c] == 5 {
					return moveNum, markedSum
				}
			}
		}
	}
	return -1, -1
}

func calcScore(winningNum, markedSum int, board Board) int {
	var boardSum = -markedSum
	for _, n := range board.data {
		boardSum += n
	}
	return boardSum * winningNum
}

func solveA(data []string) int {
	var (
		minMoveNum       = 999999
		minMoveBoard     = Board{}
		minMoveMarkedSum = 0
	)

	moves, boards := parseMovesAndBoards(data)
	for _, board := range boards {
		moveNum, markedSum := runBingo(moves, board)
		if moveNum < minMoveNum {
			minMoveNum = moveNum
			minMoveBoard = board
			minMoveMarkedSum = markedSum
		}
	}

	log.Print(minMoveNum, moves[minMoveNum])
	log.Print(minMoveBoard, minMoveMarkedSum)
	return calcScore(moves[minMoveNum], minMoveMarkedSum, minMoveBoard)
}

func solveB(data []string) int {
	var (
		maxMoveNum       = 0
		maxMoveBoard     = Board{}
		maxMoveMarkedSum = 0
	)

	moves, boards := parseMovesAndBoards(data)
	for _, board := range boards {
		moveNum, markedSum := runBingo(moves, board)
		if moveNum > maxMoveNum {
			maxMoveNum = moveNum
			maxMoveBoard = board
			maxMoveMarkedSum = markedSum
		}
	}

	log.Print(maxMoveNum, moves[maxMoveNum])
	log.Print(maxMoveBoard, maxMoveMarkedSum)
	return calcScore(moves[maxMoveNum], maxMoveMarkedSum, maxMoveBoard)

}
