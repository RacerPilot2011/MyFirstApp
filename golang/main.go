package main

import (
	"runtime"
	"time"

	project "example.com/golang/programs"
)

func main() {
	if runtime.GOOS == "windows" {
		project.W()
	} else {
		project.Mal()
	}
	println("Welcome to my golang projects!")
	time.Sleep(2 * time.Second)
	println("What program do you want to run?")
	project.Choose()
}
