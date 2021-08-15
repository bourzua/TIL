package com.example.cosinesimilarity.controller;

import com.example.cosinesimilarity.dto.MemberDto;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class MemberController {

    @GetMapping("/join")
    public String joinPage(Model model){
        model.addAttribute("memberDto", new MemberDto());
        return "join";
    }

    @PostMapping("/join")
    public String joinRequest(MemberDto memberDto) {

    }


}
