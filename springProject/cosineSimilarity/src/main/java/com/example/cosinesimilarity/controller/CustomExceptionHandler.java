package com.example.cosinesimilarity.controller;

import com.example.cosinesimilarity.dto.LoginDto;
import com.example.cosinesimilarity.dto.MemberDto;
import com.example.cosinesimilarity.exception.CustomJoinException;
import com.example.cosinesimilarity.exception.LoginException;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class CustomExceptionHandler {

    @ExceptionHandler({CustomJoinException.class})
    public String CustomJoinException(CustomJoinException e, Model model) {
        model.addAttribute("memberDto", new MemberDto());
        model.addAttribute("errorMessage", e.getMessage());
        return "join";
    }

    @ExceptionHandler({LoginException.class})
    public String LoginException(Model model) {
        model.addAttribute("loginDto", new LoginDto());
        model.addAttribute("errorMessage", "아이디 혹은 비밀번호가 다릅니다.");
        return "login";
    }
}
