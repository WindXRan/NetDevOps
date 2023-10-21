# HTTP

## Brief introduction

HTTP（Hypertext Transfer Protocol）是一种用于在Web上进行通信的应用层协议。它是一种客户端-服务器协议，用于在Web浏览器和Web服务器之间传输超文本数据。

HTTP的基本工作原理是，客户端发送一个HTTP请求到服务器，服务器根据请求进行处理，并生成一个HTTP响应返回给客户端。HTTP使用一种无状态的请求-响应模型，每个请求都是独立的，且服务器不会记住之前的请求历史。

## URL

HTTP URL (Uniform Resource Locator) 是用于标识和定位资源的地址，常用于在 Web 浏览器中访问网页、图片、视频等资源。HTTP URL 由以下几个部分组成：

1. 协议 (Protocol)：指定使用的协议，通常是 "http://" 表示使用 HTTP 协议。在加密传输时，可以使用 "https://" 表示使用 HTTPS 协议。
2. 主机名 (Host)：指定服务器的域名或 IP 地址，表示要访问的资源所在的主机。
3. 端口号 (Port)：可选项，如果没有明确指定，默认为协议的默认端口号。例如，HTTP 的默认端口号为 80，HTTPS 的默认端口号为 443。当使用非默认端口号时，需要在主机名后加上 ":端口号"，如 "[example.com:8080](http://example.com:8080/)"。
4. 路径 (Path)：指定服务器上资源的路径，可以是一个文件路径或目录路径。以 "/" 开头，按照层级结构指定资源所在的位置。例如 "/images/photo.jpg"，表示在服务器上的 images 目录下的 photo.jpg 文件。
5. 查询参数 (Query Parameters)：可选项，用于向服务器传递额外的参数信息。以 "?" 开头，多个参数之间使用 "&" 分隔。例如 "?id=123&category=books"，表示传递了两个参数：id 和 category。
6. 锚点 (Fragment)：可选项，用于在页面中定位到指定位置。以 "#" 开头，后面跟着锚点的名称或 ID。例如 "#section1"，表示页面加载后会自动滚动到拥有 "section1" 锚点的位置。

综合起来，一个完整的 HTTP URL 的格式如下所示：

```
协议://主机名[:端口号]/路径[?查询参数]#锚点
```

示例：

```
http://www.example.com/index.html
https://api.example.com/v1/users?id=123
http://127.0.0.1:8080/images/photo.jpg
```

HTTP URL 提供了一种统一的方式来定位和访问互联网上的各种资源，浏览器通过解析 URL 可以向服务器发起请求，并获取响应的资源。

## HTTP Request

HTTP 请求是客户端向服务器发出的请求，用于获取或提交资源。HTTP 请求由三个部分组成：**请求行、消息头和消息体。**

1. **请求行**由请求**Method**, **URL** 字段和**HTTP Version**三部分构成, 总的来说请求行就是定义了本次请求的请求方式, 请求的地址, 以及所遵循的HTTP协议版本例如：

```text
GET /example.html HTTP/1.1 (CRLF)
```

2. **消息头**是 HTTP 请求或响应消息中的一部分，用于在请求或响应中携带附加信息，以便服务器或客户端处理请求或响应。HTTP 消息头通常**由一个或多个字段组成**，**每个字段都包含一个名称和一个值，两者之间使用冒号（:）隔开。**

   ```
   Header: value
   ```

HTTP 消息头包含两个部分，即**通用头部和实体头部**。**通用头部**用于描述消息本身的信息，如日期、缓存控制等。而**实体头部**则对消息中包含的主体进行描述，如内容长度、内容类型等。

```
常见的 HTTP 消息头包括：

1. `Accept：指定客户端能够接收的服务端响应的数据类型。`
2. `Content-Type：指定请求或响应消息的内容类型，如 text/html、application/json 等。`
3. `Content-Length：指定消息主体的长度。`
4. `User-Agent：表示客户端的身份标识，通常是浏览器型号及版本信息。`
5. `Host：表示客户端希望访问的服务器主机名或域名。`
6. `Cookie：用于客户端与服务器之间的会话跟踪。`
7. `Cache-Control：指定请求或响应消息的缓存控制策略。`
8. `Connection：指定连接管理策略，如 keep-alive、close 等。
```

需要注意的是，HTTP 消息头具有一定的灵活性，客户端和服务器可以根据需要自定义消息头，以传递额外的元数据信息。但是，如果过多地使用自定义消息头，将会影响接收方的可移植性。

以下是一个 HTTP 响应消息头的示例：

```
Copy CodeHTTP/1.1 200 OK
Content-Type: text/html;charset=utf-8
Content-Length: 1024
Cache-Control: no-cache, no-store, must-revalidate
Server: Apache/2.4.51 (Unix)
Date: Thu, 21 Oct 2023 07:16:03 GMT
```

3. **消息体**是一些额外的参数信息，通常在 **POST** 请求中使用，用于向服务器传递**表单数据、JSON 数据**等信息。消息体的长度由 Content-Length 请求头指定。

综合起来，一个 HTTP 请求的格式如下：

```
请求方法 URL HTTP/协议版本号
Header1: value1
Header2: value2
...
HeaderN: valueN
消息体
```

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Pragma: no-cache
Cache-Control: no-cache
```

以上是一个典型的 GET 请求的示例，其中请求方法为 GET，URL 为 "/index.html"，HTTP 协议版本号为 HTTP/1.1。消息头包括 Accept、User-Agent、Accept-Encoding 等请求头信息。该请求没有消息体，因为 GET 请求通常不需要传递额外的参数信息。



## Http Response

HTTP 响应是服务器对客户端的请求所发送的回应。它由服务器发送给客户端，包含了请求的结果及相关的元数据。

HTTP 响应通常由以下几个部分组成：

1. **状态行**：状态行包含了HTTP版本号、状态码和相应的状态信息。例如，一个状态行可能是这样的：

   ```
   HTTP/1.1 200 OK
   ```

   其中，"HTTP/1.1"表示HTTP的**版本号**，"200"是**状态码**，"OK"是对**状态码的简短描述。**

   ```
   HTTP响应状态码用于表示服务器对请求的处理结果，通常由三位数字组成。以下是一些常见的HTTP响应状态码及其含义：
   
   100 Continue：客户端应该继续发送请求。这个状态码通常是由服务器在收到带有Expect请求头的请求时发送的，用于告知客户端可以继续向服务器发送请求内容。
   
   101 Switching Protocols：服务器已经理解了客户端的请求，并将通过Upgrade头通知客户端采用不同的协议来处理请求。
   
   102 Processing：服务器正在处理请求并将在未来给出一个非终止响应。
   
   200 OK：请求成功。服务器成功处理了请求，并返回了相应的内容。
   
   201 Created：已创建。服务器成功处理了请求，并在响应中创建了新的资源。
   
   204 No Content：无内容。服务器成功处理了请求，但没有返回任何内容。
   
   
   301 Moved Permanently：永久重定向。请求的资源已被永久移动到新的URL，请更新您的书签或链接。
   
   302 Found / 303 See Other：临时重定向。请求的资源已被临时移动到新的URL。
   
   400 Bad Request：错误的请求。服务器无法理解或处理请求的语法。
   
   401 Unauthorized：未授权。请求要求身份验证。客户端需要提供有效的身份验证凭据。
   
   403 Forbidden：禁止访问。服务器拒绝请求访问资源。
   
   404 Not Found：未找到。服务器无法找到请求的资源。
   
   500 Internal Server Error：服务器内部错误。服务器遇到了意外情况，无法完成请求。
   
   502 Bad Gateway：错误的网关。服务器作为网关或代理，从上游服务器接收到无效的响应。
   
   503 Service Unavailable：服务不可用。服务器暂时无法处理请求。
   ```

   

2. **响应头**：响应头包含了与响应相关的元数据信息。它以键值对的形式表示，并以一行一对的方式进行分隔。常见的响应头字段有：

   - Content-Type：指示响应正文中的数据类型。例如，text/html 表示响应是HTML文档。
   - Content-Length：指示响应正文的长度（以字节为单位）。
   - Server：指示提供响应的服务器软件名称和版本号。

3. **空行**：空行用于分隔响应头和响应正文。

4. **响应正文**：响应正文包含了服务器返回的实际数据。它可以是任何形式的数据，例如HTML文档、JSON数据、图像等。

例如，一个完整的HTTP响应可能如下所示：

```
Copy CodeHTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 123
Server: Apache

<!DOCTYPE html>
<html>
<head>
    <title>Example</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
```

这个响应表示服务器成功处理了客户端的请求（状态码200），响应正文是一个HTML文档，内容为一个简单的网页，其中包含一个标题为"Hello, World!"的大标题。

通过解析HTTP响应，客户端可以获取服务器返回的数据和相关的元信息，并根据需要进行相应的处理。

## HTTP的五大特点

1. 支持**客户/服务器**模式。
2. **简单快速**：客户向服务器请求服务时，只需传送请求方法和路径。请求方法常用的有`GET`、`HEAD`、`POST`。每种方法规定了客户与服务器联系的类型不同。由于`HTTP`协议简单，使得`HTTP`服务器的程序规模小，因而通信速度很快。
3. **灵活**：HTTP允许传输任意类型的数据对象。正在传输的类型由`Content-Type`加以标记。
4. **无连接**：无连接的含义是限制每次连接只处理一个请求。服务器处理完客户的请求，并收到客户的应答后，即断开连接。采用这种方式可以节省传输时间。早期这么做的原因是请求资源少，追求快。后来通过`Connection: Keep-Alive`实现长连接
5. **无状态**：`HTTP`协议是无状态协议。无状态是指协议对于事务处理没有记忆能力。缺少状态意味着如果后续处理需要前面的信息，则它必须重传，这样可能导致每次连接传送的数据量增大。另一方面，在服务器不需要先前信息时它的应答就较快。

## 非持久连接和持久连接

在实际的应用中，客户端往往会发出一系列请求，接着服务器端对每个请求进行响应。对于这些请求|响应，如果每次都经过一个单独的TCP连接发送，称为**非持久连接**。反之，如果每次都经过相同的TCP连接进行发送，称为**持久连接**。

非持久连接给服务器带来了沉重的负担，每台服务器可能同时面对数以百计甚至更多的请求。持久连接就是为了解决这些问题，其特点是一直保持TCP连接状态，直到遇到明确的中断要求之后再中断连接。持久连接减少了通信开销，节省了通信量。

![HTTP协议介绍 | Linux运维部落](https://ts1.cn.mm.bing.net/th/id/R-C.2abfbb2557822d77ffad46cbfdc6c663?rik=TQd1vdkcSMut6g&riu=http%3a%2f%2fwww.178linux.com%2fwp-content%2fuploads%2f2018%2f06%2f%e6%8c%81%e4%b9%85%e8%bf%9e%e6%8e%a5.png&ehk=r14gk3gPUH7MFfsM6ZoXh%2b7OfUwMX3SDyy%2bZyBaDeAo%3d&risl=&pid=ImgRaw&r=0)

## HTTPS

**HTTPS**是一种基于**TLS**（Secure Socket Layer）/**SSL**（Secure Socket Layer）协议的HTTP协议。它通过使用数据加密和身份验证来保护网络通信安全。

在HTTPS中，TLS/SSL协议用于在客户端和服务器之间建立一条安全的通信管道。在通信过程中，TLS/SSL协议可以将所有的数据加密，从而防止黑客窃取传输中的敏感信息。

HTTPS的主要特点包括：

1. 数据加密：HTTPS使用公开密钥加密算法进行数据加密，确保数据传输过程中不被黑客窃听、篡改或冒充。
2. 身份验证：HTTPS使用数字证书来进行服务器和客户端的身份验证，确保通信双方的身份合法。
3. 安全性高：HTTPS可以有效地防止黑客攻击和数据泄露等安全问题，保障用户的隐私和信息安全。

虽然HTTPS具有很高的安全性，但其与HTTP相比，会增加一些通信开销，因为数据需要加密和解密。此外，HTTPS通常需要使用数字证书，这也会增加一些运营成本。