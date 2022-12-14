package main

import (
	"os"
	"os/exec"
)

func main(){
	dirname, _ := os.UserHomeDir()
	print(dirname)
	os.Chdir(dirname)
	os.Chdir("Documents")
	out, _ := exec.Command("mkdir test").Output()
	output := string(out[:])
	println(output)
}