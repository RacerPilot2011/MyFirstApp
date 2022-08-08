package project

import (
	"fmt"
	"math/rand"
	"runtime"
	"time"

	"github.com/manifoldco/promptui"
)

func Tell() {
	if runtime.GOOS == "windows" {
		W()
	} else {
		Mal()
	}

	fmt.Println("Welcome to the future telling program!")
	time.Sleep(2 * time.Second)
	loop()
}
func loop() {
	for i := 0; i < 2; i++ {
		fmt.Println("What is your yes or no question for future telling?")
		var what string
		fmt.Scanln(&what, &what, &what, &what, &what, &what, &what, &what, &what, &what, &what, &what, &what, &what, &what, &what, &what, &what, &what, &what, &what, &what, &what, &what,)
		rand.Seed(time.Now().UnixNano())
		min := 1
		max := 3
		dir := rand.Intn(max-min+1) + min
		fmt.Println("Seeing the future...")
		time.Sleep(3 * time.Second)
		if dir == 1 {
			fmt.Println("My sources say yes")
		}
		if dir == 2 {
			fmt.Println("Sorry,no")
		}
		if dir == 3 {
			fmt.Println("The future is foggy, ask again later")
		}
		if i == 0 {
			println("2 more future left")
		}
		if i == 1 {
			println("1 more future left")
		}
	}
	time.Sleep(1 * time.Second)
	a()
}
func a() {
	fmt.Println(ay())
	fmt.Println(ay())
	fmt.Println(ay())
}
func ay() bool {
	prompt := promptui.Select{
		Label: "Do you want to get more futures fortold, exit the whole program, or do another program?",
		Items: []string{"More Futures", "Exit", "Another Program"},
	}
	_, result, _ := prompt.Run()
	if result == "More Futures" {
		loop()
	}
	if result == "Exit" {
		println("Exiting...")
		time.Sleep(2 * time.Second)
		if runtime.GOOS == "windows" {
			Exitw()
		} else {
			Exitmal()
		}
	}
	if result == "Another Program" {
		println("Running...")
		time.Sleep(2 * time.Second)
		Againf()
	}

	return result == ""
}
