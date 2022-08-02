package project

import (
	"fmt"
	"runtime"
	"strconv"
	"time"

	"github.com/manifoldco/promptui"
)

func Cal() {
	if runtime.GOOS == "windows" {
		W()
	} else {
		Mal()
	}
	fmt.Println("Welcome to the calculator!")
	time.Sleep(2 * time.Second)
	fmt.Println("Remember to add spaces in between the numbers a operator.Type exit to exit at any time.")
	time.Sleep(2 * time.Second)
	imput()
}

func imput() {
	for {
		fmt.Println("What do you want to be calculated?")
		var What string
		var do string
		var you string
		fmt.Scanln(&What, &do, &you)
		if What == "exit" {
			con()
		}
		Whati, error := strconv.Atoi(What)
		youi, error2 := strconv.Atoi(you)
		if error != nil {
			invalidi()
		}
		if error2 != nil {
			invalidi()
		}
		fmt.Println("Calculating...")
		time.Sleep(2 * time.Second)
		if do == "+" {
			an := Whati + youi
			fmt.Println(an)
		}
		if do == "-" {
			an := Whati - youi
			fmt.Println(an)
		}
		if do == "/" {
			an := Whati / youi
			fmt.Println(an)
		}
		if do == "*" {
			an := Whati * youi
			fmt.Println(an)
		}
		time.Sleep(2 * time.Second)
	}
}
func invalidi() {
	fmt.Println("Invalid imput. Plese try again")
	imput()
}
func con() {
	fmt.Println(try())
	fmt.Println(try())
}
func try() bool {
	prompt := promptui.Select{
		Label: "Doy you want to exit the whole program or choose another program?",
		Items: []string{"Exit", "Another Program"},
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
	if result == "Another Program" {
		Againc()
	}

	return result == ""
}
