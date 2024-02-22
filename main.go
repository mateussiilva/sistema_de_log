package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	name_file := "teste.html"
	data, err := os.ReadFile(name_file)
	if err != nil{
		log.Fatal("Erro ao abrir o arquivo")
	}
	var data_string string = string(data) 
	fmt.Println(strings.Split(data_string, "\n"))	
}	