package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

const problemNumber = 2

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

	var (
		hPos = 0
		vPos = 0
	)
	for _, lineStr := range data {
		var splitString = strings.Split(lineStr, " ")
		if len(splitString) == 1 {
			continue
		}
		lineVal, _ := strconv.Atoi(splitString[1])
		switch splitString[0] {
		case "forward":
			hPos += lineVal
		case "up":
			vPos -= lineVal
		case "down":
			vPos += lineVal
		}
	}

	return hPos * vPos
}

func solveB(data []string) int {

	var (
		hPos = 0
		vPos = 0
		aim  = 0
	)
	for _, lineStr := range data {
		var splitString = strings.Split(lineStr, " ")
		if len(splitString) == 1 {
			continue
		}
		lineVal, _ := strconv.Atoi(splitString[1])
		switch splitString[0] {
		case "forward":
			hPos += lineVal
			vPos += (aim * lineVal)
		case "up":
			//vPos -= lineVal
			aim -= lineVal
		case "down":
			//vPos += lineVal
			aim += lineVal
		}
	}

	return hPos * vPos
}
