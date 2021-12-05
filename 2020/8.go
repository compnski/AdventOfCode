package main

import (
	"io/ioutil"
	"log"
	"regexp"
	"strconv"
	"strings"
)

var patt = regexp.MustCompile(`(\w{3}) ([+-]\d+)`)

func main() {
	data, _ := ioutil.ReadFile("/home/jason/src/aoc/8.txt")
	lines := strings.Split(string(data), "\n")

	for i := 0; i < len(lines); i++ {
		var (
			ip     int
			acc    int
			ipList []int
		)

		var seen = map[int]bool{}
		for {
			var line = lines[ip]
			matches := patt.FindAllStringSubmatch(line, -1)
			if len(matches) == 0 {
				log.Printf("Done! Acc = %d", acc)
				return
			}
			instr := matches[0][1]
			val, _ := strconv.Atoi(matches[0][2])

			if ip == i {
				log.Printf("SWAPPING? %s", instr)
				if instr == "nop" {
					instr = "jmp"
				} else if instr == "jmp" {
					instr = "nop"
				}
			}

			log.Printf("IP=%3d INSTR=%s VAL=%3d ACC=%5d", ip, instr, val, acc)
			if seen[ip] {
				log.Printf("LOOP")
				break
			} else {
				ipList = append(ipList, ip)
			}
			seen[ip] = true

			switch instr {
			case "acc":
				acc += val
			case "jmp":
				ip += val
				continue
			case "nop":

			}

			ip++
		}
	}
}
