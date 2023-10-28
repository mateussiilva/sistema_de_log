package main

import (
	// "fmt"
	"fmt"
	"os"
)

// func read_args(args []string) []string {
// 	if len(args) > 1{
// 		return args
// 	}
// 	os.Exit(1)
// 	return []string{}
// }


func main() {

	e := os.Rename("teste.txt","novo_teste.txt")
	// fmt.Println("Arquivo renomeado com sucesso")
	fmt.Println(e)
}
