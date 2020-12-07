package main

import (
	"io/ioutil"
	"log"
	"regexp"
	"strings"
)

func main() {
	data, _ := ioutil.ReadFile("/home/jason/src/aoc/6.txt")
	groups := regexp.MustCompile("\n\n").Split(strings.TrimRight(string(data), "\n"), -1)

	var acc int
	for _, g := range groups {
		words := strings.Split(g, "\n")
		qs := map[rune]int{}
		for _, word := range words {
			found := map[rune]bool{}
			for _, r := range word {
				if exists, _ := found[r]; !exists {
					found[r] = true
					qs[r]++
				}
			}
			log.Print(word, qs)
		}
		cnt := len(words)
		log.Print("\n", g)
		var oldAcc = acc
		for q, ansCnt := range qs {
			if ansCnt >= cnt {
				log.Print(acc, q, ansCnt, qs)
				acc++
			}
		}
		log.Print("Found: ", acc-oldAcc)
	}
	log.Print(acc)
	log.Print("#groups ", len(groups))
}
