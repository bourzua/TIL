package controller;

import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.BufferedReader;
import java.io.IOException;

public class ApiExplorer {
    public static void main(String[] args) throws IOException {
    	
    	// StringBuilder: String과 문자열을 더할 때 새로운 객체를 생성하는 것이 아니라 기존의 데이터에 더하는 방식을 사용 => 상대적으로 속도가 빠르고 부하가 적음
        StringBuilder urlBuilder = new StringBuilder("http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo?serviceKey=4IISLhc2KqHWtj3FxcnQqAeYIPd27Bh3DZyR1vgne1WLCf7s5X4ufzpbeGcQZEPVws8qSA5w8pGbpwXf5T8OWg%3D%3D&returnType=json&numOfRows=100&pageNo=1&year=2020&itemCode=PM10"); /*URL*/
        URL url = new URL(urlBuilder.toString());
        // url을 통해 HttpURLConnection 클래스 생성
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        // 헤더의 메소드 정의
        conn.setRequestMethod("GET");
        // 헤더의 Content-type 정의
        conn.setRequestProperty("Content-type", "application/json");
//        System.out.println("Response code: " + conn.getResponseCode());
        
        
        
        
        BufferedReader rd;
        if(conn.getResponseCode() >= 200 && conn.getResponseCode() <= 300) {
            rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        } else {
            rd = new BufferedReader(new InputStreamReader(conn.getErrorStream()));
        }
//        StringBuilder sb = new StringBuilder();
        String line;
        
        ObjectMapper mapper = new ObjectMapper();
        line = rd.readLine();
        
        Map<String, Map> map = mapper.readValue(line, Map.class);
        
        Map<Map, Map> map2 = map.get("response");
        Map<Map, Map> map3 = map2.get("body");
        
        ArrayList al = new ArrayList();
        
        
        
//        System.out.println(map);
//        System.out.println(map2);
//        System.out.println(map3);
        
        al = (ArrayList) map3.get("items");
        
        ArrayList<Map<String, String>> apiList = new ArrayList<Map<String,String>>();
        
        for (int i = 0; i < al.size(); i++) {
//        	System.out.println(al.getClass().getName());
//        	System.out.println(al.get(i));
        	Map<String, String> please = (Map<String, String>) al.get(i);
        	
        	String districtName = please.get("districtName");
        	String dataDate = please.get("dataDate");
        	String issueGbn = please.get("issueGbn");
        	
        	Map<String, String> one = new HashMap<String, String>();
        	one.put("districtName", districtName);
        	one.put("dataDate", dataDate);
        	one.put("issueGbn", issueGbn);
        	
        	apiList.add(one);
        	
        }
        
        System.out.println(apiList);
        
        
        

//        while ((line = rd.readLine()) != null) {
//            sb.append(line);
//        }
//        rd.close();
        conn.disconnect();
//        System.out.println(sb.toString());
    }
}