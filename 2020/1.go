package main

import (
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func main() {
	data, _ := ioutil.ReadFile("1.txt")
	snums := strings.Split(string(data), "\n")
	nums := make([]int, len(snums))
	for idx, n := range snums {
		nums[idx], _ = strconv.Atoi(n)
	}
	for idx, n := range nums {
		for jdx, m := range nums[idx:] {
			for _, o := range nums[jdx:] {
				if n+m+o == 2020 {
					log.Print(n, m, o, o*n*m)
				}
			}
		}
	}
}
