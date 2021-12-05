package main

import (
	"io/ioutil"
	"log"
	"strings"
)

func main() {
	var (
		data, _ = ioutil.ReadFile("3.txt")
		lines   = strings.Split(string(data), "\n")
		height  = len(lines)
		width   = len(lines[0])
	)

	isTree := func(r, c int) bool {
		log.Print(r, c)
		return lines[r][c%width] == '#'
	}

	log.Print("Got ", width, "  x ", height)

	checkSlope := func(dR, dC int) int64 {
		var acc int64
		var cC, cR int
		for cR < height-1 {
			if isTree(cR, cC) {
				acc++
			}
			cR += dR
			cC += dC
		}
		log.Print([]int{dR, dC, cC, cR})
		return acc
	}
	log.Print("Acc ", checkSlope(1, 1)*
		checkSlope(1, 3)*
		checkSlope(1, 5)*
		checkSlope(1, 7)*
		checkSlope(2, 1))
}
