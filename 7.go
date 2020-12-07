package main

import (
	"io/ioutil"
	"log"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	//light salmon bags contain 5 dark brown bags, 2 dotted coral bags, 5 mirrored turquoise bags.
	//drab magenta bags contain 1 vibrant purple bag, 5 dark lime bags, 2 clear silver bags.
	bagPattern := regexp.MustCompile(`(?:(\w+ \w+)? bags? contain)?(?:\s([\dno]+)\s(\w+\s?\w*)\sbags?)+`)
	data, _ := ioutil.ReadFile("/home/jason/src/aoc/7.txt")
	bags := regexp.MustCompile("\n").Split(strings.TrimRight(string(data), "\n"), -1)

	canContainMap := map[string]map[string]int{}

	for _, bag := range bags {
		bagParts := strings.Split(bag, ",")
		var container string
		for _, b := range bagParts {

			matches := bagPattern.FindAllStringSubmatch(b, -1)[0]
			if matches[1] != "" {
				container = matches[1]
			}
			count, _ := strconv.Atoi(matches[2])
			innerBag := matches[3]
			//log.Printf("%d %s inside %s", count, innerBag, container)
			if _, exists := canContainMap[innerBag]; !exists {
				canContainMap[innerBag] = map[string]int{}
			}
			if _, exists := canContainMap[innerBag][container]; exists {
				log.Fatal("Already have mapping for ", b)
			}

			canContainMap[innerBag][container] = count
		}
	}
	log.Print(canContainMap["shiny gold"])
	acc, colors := canContain(canContainMap, "shiny gold")

	log.Print(len(visited)-1, acc, len(colors))
	log.Print("Done")
}

var visited = map[string]bool{}

func canContain(canContainMap map[string]map[string]int, color string) (acc int, colors []string) {
	if _, exists := visited[color]; exists {
		//	return
	}
	visited[color] = true

	if _, exists := canContainMap[color]; !exists {
		acc = 1
		return
	}
	for color := range canContainMap[color] {
		cnt, c := canContain(canContainMap, color)
		acc += cnt
		colors = append(colors, color)
		colors = append(colors, c...)
	}
	return
}
