package main

import (
	"log"
	"net/http"

	"sample/go-socket.io"
)

func main() {
	server, err := socketio.NewServer(nil)
	if err != nil {
		log.Fatal(err)
	}

	count := 1

	server.On("connection", func(so socketio.Socket) {
		count++
		log.Println("connect :", count)

		so.On("test", func(msg string) {
			log.Println(msg)
		})

		so.On("disconnection", func() {
			log.Println("on disconnect")
		})
	})
	server.On("error", func(so socketio.Socket, err error) {
		log.Println("error:", err)
	})

	http.Handle("/socket.io/", server)
	log.Println("Serving at localhost:5000...")
	log.Fatal(http.ListenAndServe(":5000", nil))
}
