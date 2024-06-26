# RPC- Client-Server Architecture with FTP Communication Protocol

### FTP stands for File Transfer Protocol, which is a standard network protocol used for transferring files between a client and a server on a computer network. In the context of your client-server architecture project, implementing FTP means setting up a mechanism for clients to transfer files to and from the server using predefined commands and protocols.


This project implements a client-server architecture where the communication protocol is FTP based. It supports multiple clients, and each client's multiple requests are handled by the respective servers to which they make the request.

## Features

* **Addition**
  * Description: Performs addition of two numbers.
  * Command: `ADD x y`
* **Subtraction**
  * Description: Performs subtraction of two numbers.
  * Command: `SUBTRACT x y`
* **Multiplication**
  * Description: Performs multiplication of two numbers.
  * Command: `MULTIPLY x y`
* **Increment** (Optional)
  * Description: Increments a given number.
  * Command: `INCREMENT x`
* **LOOKUP** (Main Server Only)
  * Description: Provides information lookup.
  * Command: `LOOKUP keyword`



## Usage

1. **Server Setup**
   * Run `server.py` on multiple machines to set up distributed servers.
2. **Client Usage**
   * Run `client.py` on each client machine.
   * Use the specified commands (`ADD`, `SUBTRACT`, `MULTIPLY`, `INCREMENT`, `LOOKUP`) followed by the necessary arguments
