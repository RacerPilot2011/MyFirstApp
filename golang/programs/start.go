package project

import (
	"fmt"
	"time"

	"github.com/manifoldco/promptui"
)

func Choose() {
	fmt.Println(yesNo())
	fmt.Println(yesNo())
	fmt.Println(yesNo())
}
func yesNo() bool {
	prompt := promptui.Select{
		Label: "Do you want to use the Calculator, play the Guessing Game, or ask the Future Teller(beta)?",
		Items: []string{"Calculator", "Guessing Game", "Future Teller(beta)"},
	}
	_, result, _ := prompt.Run()
	if result == "Guessing Game" {
		println("Running...")
		time.Sleep(2 * time.Second)
		Guess()
	}
	if result == "Future Teller(beta)" {
		println("Running...")
		time.Sleep(2 * time.Second)
		Tell()
	}
	if result == "Calculator" {
		println("Running...")
		time.Sleep(2 * time.Second)
		Cal()
	}

	return result == ""
}
