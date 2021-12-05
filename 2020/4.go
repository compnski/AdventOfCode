package main

import (
	"io/ioutil"
	"log"
	"regexp"
	"strconv"
	"strings"
)

func validYear(y string, min, max int) bool {
	yr, _ := strconv.Atoi(y)
	return yr >= min && yr <= max
}

func validHeight(h string) bool {
	if strings.HasSuffix(h, "cm") {
		h = strings.ReplaceAll(h, "cm", "")
		hi, _ := strconv.Atoi(h)
		return hi >= 150 && hi <= 193
	} else if strings.HasSuffix(h, "in") {
		h = strings.ReplaceAll(h, "in", "")
		hi, _ := strconv.Atoi(h)
		return hi >= 59 && hi <= 76
	}
	return false
}

var hairPattern = regexp.MustCompile("^#[0-9a-f]{6}$")
var eyePattern = regexp.MustCompile("^amb|blu|brn|gry|grn|hzl|oth$")
var pidPattern = regexp.MustCompile("^\\d{9}$")

func validHair(h string) bool {
	return hairPattern.MatchString(h)
}
func validEye(h string) bool {
	return eyePattern.MatchString(h)
}
func validPid(h string) bool {
	return pidPattern.MatchString(h)
}

func isValid(record string) int {
	foundF := map[string]string{}
	fields := strings.Split(record, " ")
	for _, field := range fields {
		fparts := strings.Split(field, ":")
		if len(fparts) > 1 {
			foundF[fparts[0]] = fparts[1]
		}
	}

	if validYear(foundF["byr"], 1920, 2002) &&
		validYear(foundF["iyr"], 2010, 2020) &&
		validYear(foundF["eyr"], 2020, 2030) &&
		validHeight(foundF["hgt"]) &&
		validHair(foundF["hcl"]) &&
		validEye(foundF["ecl"]) &&
		validPid(foundF["pid"]) {
		return 1
	}
	return 0
}

func main() {
	data, _ := ioutil.ReadFile("/home/jason/src/aoc/3.txt")
	lines := strings.Split(string(data), "\n")
	var (
		acc      string
		numValid int
	)

	for _, line := range lines {
		if line == "" {
			numValid += isValid(acc)
			acc = ""
		}
		acc += line + " "
	}
	log.Print(numValid)
}
