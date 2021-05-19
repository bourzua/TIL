<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

	<c:forEach var="object" items="${realZZIN}">
	<c:forEach var="obj" items="${object}">
		${obj}<br>
	</c:forEach>
	<hr>
	</c:forEach>

</body>
</html>