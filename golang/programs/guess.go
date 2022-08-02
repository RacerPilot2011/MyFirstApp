package project

import (
	"fmt"
	"math/rand"
	"runtime"
	"strconv"
	"time"

	"github.com/manifoldco/promptui"
)

func Guess() {
	if runtime.GOOS == "windows" {
		W()
	} else {
		Mal()
	}
	fmt.Println("Welcome to the Guess The Number game!")
	time.Sleep(2 * time.Second)
	fmt.Println("Guess a number between 1 and 100")
	game()
}
func game() {
	rand.Seed(time.Now().UnixNano())
	min := 1
	max := 100
	n := rand.Intn(max-min+1) + min
	var op int = 101
	time.Sleep(2 * time.Second)
	for {
		fmt.Println("What is your guess?")
		var guess string
		fmt.Scanln(&guess)
		answer, err := strconv.Atoi(guess)
		if err != nil {
			invalidloop()
		}
		if answer == n {
			fmt.Println("You guessed the number!")
			fmt.Println(yesNog())
			fmt.Println(yesNog())
		}
		if answer > n {
			fmt.Println("Less Than")
		}
		if answer < n {
			fmt.Println("Greater Than")
		}
		if answer > op {
			fmt.Println("Invalid guess. The number is between 1 and 100")
		}
	}
}
func invalidloop() {
	println("Invalid imput.Please type a number and try again.")
	game()
}
func yesNog() bool {
	prompt := promptui.Select{
		Label: "Doy you want, play again, to exit the whole program, or choose another program?",
		Items: []string{"Play Again", "Exit", "Another Program"},
	}
	_, result, _ := prompt.Run()
	if result == "Exit" {
		println("Exiting...")
		time.Sleep(2 * time.Second)
		if runtime.GOOS == "windows" {
			Exitw()
		} else {
			Exitmal()
		}
	}
	if result == "Play Again" {
		if runtime.GOOS == "windows" {
			W()
		} else {
			Mal()
		}
		game()
	}
	if result == "Another Program" {
		Againg()
	}

	return result == ""
}
