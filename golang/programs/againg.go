package project

import (
	"fmt"
	"time"

	"github.com/manifoldco/promptui"
)

func Againg() {
	fmt.Println(yesNoag())
	fmt.Println(yesNoag())
}
func yesNoag() bool {
	prompt := promptui.Select{
		Label: "Do you want to use the Calculator or ask the Future Teller(beta)?",
		Items: []string{"Calculator", "Future Teller(beta)"},
	}
	_, result, _ := prompt.Run()
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
