package com.example.cosinesimilarity.controller;

import com.example.cosinesimilarity.entity.Member;
import com.example.cosinesimilarity.service.MovieService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import javax.servlet.http.HttpSession;

@Controller
public class IndexController {

    @Autowired
    private MovieService movieService;

    @GetMapping("/")
    public String index(Model model) {
        model.addAttribute("movieList", movieService.getAllMovies());
        return "index";
    }

}
