package project

import (
	"fmt"
	"os"
	"os/exec"
)

func Exitmal() {
	out, err := exec.Command("clear").Output()
	if err != nil {
		fmt.Printf("%s", err)
	}
	fmt.Println("Command Successfully Executed")
	output := string(out[:])
	fmt.Println(output)
	os.Exit(0)
}
func Exitw() {
	out, err := exec.Command("cls").Output()
	if err != nil {
		fmt.Printf("%s", err)
	}
	fmt.Println("Command Successfully Executed")
	output := string(out[:])
	fmt.Println(output)
	os.Exit(0)
}
func Mal() {
	out, err := exec.Command("clear").Output()
	if err != nil {
		fmt.Printf("%s", err)
	}
	fmt.Println("Command Successfully Executed")
	output := string(out[:])
	fmt.Println(output)
}
func W() {
	out, err := exec.Command("cls").Output()
	if err != nil {
		fmt.Printf("%s", err)
	}
	fmt.Println("Command Successfully Executed")
	output := string(out[:])
	fmt.Println(output)
}
