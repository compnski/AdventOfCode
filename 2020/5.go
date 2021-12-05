package main

import (
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func parseLine(s string) (r int64, c int64) {
	s = strings.ReplaceAll(s, "F", "0")
	s = strings.ReplaceAll(s, "B", "1")
	s = strings.ReplaceAll(s, "L", "0")
	s = strings.ReplaceAll(s, "R", "1")
	r, _ = strconv.ParseInt(s[0:7], 2, 8)
	c, _ = strconv.ParseInt(s[7:10], 2, 4)
	return
}

func main() {
	var seats = [128][8]int64{[8]int64{}}
	data, _ := ioutil.ReadFile("/home/jason/src/aoc/4.txt")
	lines := strings.Split(string(data), "\n")
	var (
		maxSid int64
	)

	for _, line := range lines {
		if line == "" {
			continue
		}
		r, c := parseLine(line)
		sid := r*8 + c
		seats[r][c] = sid
		if sid > maxSid {
			maxSid = sid
		}
		log.Print(line, " ", r, c)
	}
	for _, s := range seats {
		log.Print(s)
	}

}
