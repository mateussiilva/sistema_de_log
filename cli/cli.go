package main

import (
	"fmt"
	"os"
)


func read_args(args []string) []string {
	if len(args) > 1{
		return args
	}
	os.Exit(1)
	return []string{}
}


func main() {
	args := []string{}
	read_args(args)
	fmt.Print("Olá seja bem vindo a cli do LOG SISTEMAS")
}
