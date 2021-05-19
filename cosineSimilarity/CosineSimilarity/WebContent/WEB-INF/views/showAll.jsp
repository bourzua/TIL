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
	<h1>하자 좀</h1>
	<c:forEach var="object" items="${apiList}">
<%-- 		지역: ${object.districtName}<br> --%>
<%-- 		날짜: ${object.districtName}<br> --%>
<%-- 		경보여부: ${object.districtName}<br> --%>
	<c:forEach var="obj" items="${object}">
		${obj}<br>
	</c:forEach>
	<hr>
	</c:forEach>
</body>
</html>