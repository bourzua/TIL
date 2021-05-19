package controller;

import java.util.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import controller.*;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.fasterxml.jackson.databind.ObjectMapper;

import beans.CSBean;
import beans.PreBean;
import info.debatty.java.stringsimilarity.Cosine;

@Controller
public class CSController {
	
	@PostMapping("/cs1")
	public String cs1(@ModelAttribute CSBean bean) {
		
		double sum = cosineSimilarity("python", bean.getData1()) + cosineSimilarity("정보처리기사", bean.getData2());
		System.out.println(sum);
			
//		System.out.println(bean.getData1());
//		System.out.println(bean.getData2());
//		System.out.println(bean.getData3());
//		System.out.println(bean.getData4());
		
		return "csReturn";
	}
	
	public double cosineSimilarity(String str1, String str2) {

        // Let's work with sequences of 2 characters...
        Cosine cosine = new Cosine(2);

        // Pre-compute the profile of strings
        Map<String, Integer> profile1 = cosine.getProfile(str1);
        Map<String, Integer> profile2 = cosine.getProfile(str2);
        
		return cosine.similarity(profile1, profile2);
	}
	
	@PostMapping("/show")
	public String show(@ModelAttribute PreBean bean, Model model) {
		
		
		
		List<List<String>> workList = new ArrayList<List<String>>();
		
		List<Double> doubleList = new ArrayList<Double>();
		
		List<String> companyName = new ArrayList<String>();
		List<String> good = new ArrayList<String>();
		
		companyName.add("신한은행");
		companyName.add("우리은행");
		companyName.add("국민은행");
		companyName.add("하나은행");
		companyName.add("기업은행");
		
		good.add("python 정보처리기사 SQLD");
		good.add("C++ ADP");
		good.add("C 정보보안기사 SQLD");
		good.add("JAVA 정보처리산업기사 ISMP");
		good.add("GO ADSP SQLP");
		
		for (int i = 0; i < companyName.size(); i++) {
			String CN = companyName.get(i);
			String GOOD = good.get(i);
			
			double total = 0;
			total += cosineSimilarity(bean.getData1(), GOOD);
			total += cosineSimilarity(bean.getData2(), GOOD);
			total += cosineSimilarity(bean.getData3(), GOOD);
			total += cosineSimilarity(bean.getData4(), GOOD);
			
			String totalString = Double.toString(total);
			List<String> company = new ArrayList<String>();
			company.add(totalString);
			company.add(CN);
			company.add(GOOD);
			
			workList.add(company);
			
			doubleList.add(total);
		}
		Collections.sort(doubleList);
		Collections.reverse(doubleList);
		System.out.println(doubleList);
		System.out.println(workList);
		
		List<List<String>> realZZIN = new ArrayList<List<String>>();
		
		for (int i = 0; i < 5; i++) {
			
//			String S = Double.toString(doubleList.get(i));
			double S = doubleList.get(i);
			
			for (int j = 0; j < 5; j++) {
				Double A = Double.parseDouble(workList.get(j).get(0));
				if (S == A) {
					String companyName2 = workList.get(j).get(1);
					String pre2 = workList.get(j).get(2);
					
					
					List<String> p = new ArrayList<String>();
					p.add(companyName2);
					p.add(pre2);
					
					realZZIN.add(p);
				}
			}
			
		}
		
		model.addAttribute("realZZIN", realZZIN);
	
		

		
		
		return "show";
	}
	
	@GetMapping("/showAll")
	public String sa(Model model) throws IOException{
		
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
            rd = new BufferedReader(new InputStreamReader(conn.getInputStream(), "UTF-8"));
        } else {
            rd = new BufferedReader(new InputStreamReader(conn.getErrorStream(), "UTF-8"));
        }
//        StringBuilder sb = new StringBuilder();
        String line;
        
        ObjectMapper mapper = new ObjectMapper();
        line = rd.readLine();
        
        
        
        Map<String, Map> map = mapper.readValue(line, Map.class);       
        Map<String, Map> map2 = map.get("response");
        Map<String, Map> map3 = map2.get("body");
        
        ArrayList al = new ArrayList();
        
        
        System.out.println(map);
        System.out.println(map2);
        System.out.println(map3);
        
        al = (ArrayList) map3.get("items");
        
        ArrayList<ArrayList<String>> apiList = new ArrayList<ArrayList<String>>();
        
        for (int i = 0; i < al.size(); i++) {
        	
        	Map<String, String> please = (Map<String, String>) al.get(i);
        	
        	String districtName = please.get("districtName");
        	String dataDate = please.get("dataDate");
        	String issueGbn = please.get("issueGbn");

        	
        	System.out.println(districtName);
        	System.out.println(dataDate);
        	System.out.println(issueGbn);
        	
        	
//        	Map<String, String> one = new HashMap<String, String>();
//        	one.put("districtName", districtName);
//        	one.put("dataDate", dataDate);
//        	one.put("issueGbn", issueGbn);
        	
//        	System.out.println(one.get("districtName"));
        	
        	ArrayList<String> apiListSmall = new ArrayList<String>();
        	
        	apiListSmall.add(districtName);
        	apiListSmall.add(dataDate);
        	apiListSmall.add(issueGbn);
        	
        	apiList.add(apiListSmall);
        	
        }
        
        
        System.out.println(apiList);
        model.addAttribute("apiList", apiList);
        
        
        
        
        
        

//        while ((line = rd.readLine()) != null) {
//            sb.append(line);
//        }
//        rd.close();
        conn.disconnect();
//        System.out.println(sb.toString());
		
		return "showAll";
	}
	
	
}
