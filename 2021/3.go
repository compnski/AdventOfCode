package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

const problemNumber = 3

func readInputLines(inputName string) []string {
	data, _ := ioutil.ReadFile(fmt.Sprintf("/home/jason/src/advent-of-code-2021/%s", inputName))
	lines := strings.Split(string(data), "\n")
	return lines
}

func main() {

	var testInput = fmt.Sprintf("%02d.test.txt", problemNumber)
	var realInput = fmt.Sprintf("%02d.real.txt", problemNumber)
	_ = realInput
	//	log.Print("Test: ", solveA(readInputLines(testInput)))
	//log.Print("Real: ", solveA(readInputLines(realInput)))

	log.Print("Test: ", solveB(readInputLines(testInput)))
	log.Print("Real: ", solveB(readInputLines(realInput)))

}

func countBits(data []string) []int {
	var (
		stringLen = len(data[0])
		bitCount  = make([]int, stringLen)
	)
	for _, lineStr := range data {
		for idx, chr := range lineStr {

			if chr == '1' {
				bitCount[idx]++
			}
		}
	}
	return bitCount
}

func solveA(data []string) int {
	var stringLen = len(data[0])

	var bitCount = countBits(data)
	var gamma = 0
	var epsilon = 0
	log.Print(bitCount, (len(data)-1)/2)
	for i := 0; i < stringLen; i++ {
		if bitCount[i] >= (len(data)-1)/2 {
			log.Print(1)
			gamma += (1 << (stringLen - i - 1))
		} else {
			log.Print(0)
			epsilon += (1 << (stringLen - i - 1))
		}
	}
	log.Print(gamma, epsilon)
	return gamma * epsilon
}

func splitByCount(data []string, currentBitIdx int, lookingForOne bool) (ret []string) {
	var bitCount = countBits(data)
	var oneMostCommon = bitCount[currentBitIdx] > ((len(data) - 1) / 2)
	for _, line := range data {
		if len(line) <= 1 {
			continue
		}
		if lookingForOne { // oxy
			if oneMostCommon && line[currentBitIdx] == '1' {
				ret = append(ret, line)
			} else if !oneMostCommon && line[currentBitIdx] == '0' {
				ret = append(ret, line)
			}
		} else { // co2
			if !oneMostCommon && line[currentBitIdx] == '1' {
				ret = append(ret, line)
			} else if oneMostCommon && line[currentBitIdx] == '0' {
				ret = append(ret, line)
			}
		}
	}
	return
}

func findRating(data []string, forOxy bool) int64 {
	for currentBit := 0; currentBit < len(data[0]); currentBit++ {
		data = splitByCount(data, currentBit, forOxy)
		log.Print(currentBit, data)
		if len(data) == 1 {
			i, _ := strconv.ParseInt(data[0], 2, 32)
			return i
		}
	}
	return 0
}

func solveB(data []string) int64 {
	var (
		oxyRating = findRating(data, true)
		co2Rating = findRating(data, false)
	)
	return oxyRating * co2Rating

}
