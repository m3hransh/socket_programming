# Socket Programming
**This project is a Internet Engineering (Fall 2020) Project of
[Computer Engineering Bu-Ali Sina University](http://eng.basu.ac.ir/en/ce)**.
In this project, an application with following architecture is implemented:
1. There is client-app that needs some services.(at the first iteration simple mapping).
2. There is getway-server that will get the client request and connect to some services using socket.
3. There are some services that might do different things. (at the first iteration one server for translating Persian to English)
### Phases
- [x] Implementing client and getway-server that simply get some message request with some contents
- [ ] Rewriting response message in getway-server to use other services on the network
- [ ] Use Google Translation API in the service server
- [ ] Adding UI to client and servers