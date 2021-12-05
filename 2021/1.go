package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

const problemNumber = 1

func readInputLines(inputName string) []string {
	data, _ := ioutil.ReadFile(fmt.Sprintf("/home/jason/src/advent-of-code-2021/%s", inputName))
	lines := strings.Split(string(data), "\n")
	return lines
}

func main() {

	var testInput = fmt.Sprintf("%02d.test.txt", problemNumber)
	var realInput = fmt.Sprintf("%02d.real.txt", problemNumber)

	log.Print("Test: ", solveA(readInputLines(testInput)))
	log.Print("Real: ", solveA(readInputLines(realInput)))

	log.Print("Test: ", solveB(readInputLines(testInput)))
	log.Print("Real: ", solveB(readInputLines(realInput)))

}

func solveA(data []string) int {
	var prev = -1
	var depthIncreaseCount = 0
	for _, lineStr := range data {
		lineVal, _ := strconv.Atoi(lineStr)
		if prev >= 0 && lineVal > prev {
			depthIncreaseCount++
		}
		prev = lineVal
	}
	return depthIncreaseCount
}

func solveB(data []string) int {
	var depthIncreaseCount = 0
	var prevLineVal = make([]int, len(data))
	for idx, lineStr := range data {
		lineVal, _ := strconv.Atoi(lineStr)
		prevLineVal[idx] = lineVal

		if idx > 2 && lineVal > prevLineVal[idx-3] {
			depthIncreaseCount++
		}
	}
	return depthIncreaseCount
}
