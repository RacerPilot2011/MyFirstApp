package project

import (
	"fmt"
	"time"

	"github.com/manifoldco/promptui"
)

func Againc() {
	fmt.Println(yesNoc())
	fmt.Println(yesNoc())
}
func yesNoc() bool {
	prompt := promptui.Select{
		Label: "Do you want to play the Guessing Game or ask the Future Teller(beta)?",
		Items: []string{"Guessing Game", "Future Teller(beta)"},
	}
	_, result, _ := prompt.Run()
	if result == "Future Teller(beta)" {
		println("Running...")
		time.Sleep(2 * time.Second)
		Tell()
	}
	if result == "Guessing Game" {
		println("Running...")
		time.Sleep(2 * time.Second)
		Guess()
	}

	return result == ""
}
