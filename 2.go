package main

import (
	"io/ioutil"
	"log"
	"regexp"
	"strconv"
	"strings"
)

var pattern = regexp.MustCompile(`(\d+)-(\d+) (\w)`)

func checkPass(policy, passwd string) bool {
	var (
		min, _ = strconv.Atoi(pattern.FindStringSubmatch(policy)[1])
		max, _ = strconv.Atoi(pattern.FindStringSubmatch(policy)[2])
		ltr    = pattern.FindStringSubmatch(policy)[3][0]
		//ltrCnt = strings.Count(passwd, ltr)
	)
	log.Print(min, max, len(passwd))
	return (passwd[min-1] == ltr || passwd[max-1] == ltr) &&
		passwd[min-1] != passwd[max-1]
}

func main() {

	data, _ := ioutil.ReadFile("2.txt")
	lines := strings.Split(string(data), "\n")

	var acc int
	for _, line := range lines {
		l := strings.Split(line, ": ")
		policy, passwd := l[0], l[1]
		if checkPass(policy, passwd) {
			acc++
		}
	}
	log.Print("Acc ", acc)
}
