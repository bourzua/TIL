package com.example.cosinesimilarity.controller;

import com.example.cosinesimilarity.dto.MovieDto;
import com.example.cosinesimilarity.dto.RecommendKeywordDto;
import com.example.cosinesimilarity.service.RecommendService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.List;

@Controller
public class RecommendController {

    @Autowired
    private RecommendService recommendService;

    @GetMapping("/recommend")
    public String recommend(Model model) {
        model.addAttribute("recommendKeywordDto", new RecommendKeywordDto());
        return "recommend";
    }

    @PostMapping("/recommend")
    public String recommend(RecommendKeywordDto recommendKeywordDto, Model model) {
        List<MovieDto> recommend = recommendService.getRecommend(recommendKeywordDto.getKeyword());
        model.addAttribute("recommendedMovies", recommend);
        return "recommend";
    }
}
