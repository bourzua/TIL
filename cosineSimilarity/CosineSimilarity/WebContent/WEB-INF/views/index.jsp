<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1>Hello Spring MVC Java</h1>

	<!-- 	<a href='test1?data1=100&data2=200'>test1 get</a> -->
	<!-- 	<hr> -->
	<!-- 	<a href='test2?data1=100&data2=200&data3=300&data3=400'>test2 get</a> -->

	<!-- 	<a href="test1?data1=100&data2=200">test1</a> -->
	<!-- 	<hr> -->
	<!-- 	<a href="test2">test2</a> -->
	<!-- 	<hr> -->
	<!-- 	<a href="test3">test3</a> -->
	<!-- 	<hr> -->
	<!-- 	<a href="test4">test4</a> -->
	
	<form action="test1" method="post">
		data1 : <input type="text" name="data1"/>
		data2 : <input type="text" name="data2"/>
		<button type="submit">확인</button>
	</form>
	
	<a href="showAll">showAll</a>
	<hr>
	<form action="show" method="post">
		사용언어 : <input type="text" name="data1">
		자격증1 : <input type="text" name="data2">
		자격증2 : <input type="text" name="data3">
		자격증3 : <input type="text" name="data4">
		<button type="submit">검색</button>
	</form>



</body>
</html>