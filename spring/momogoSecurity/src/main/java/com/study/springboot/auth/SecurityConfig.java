package com.study.springboot.auth;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.access.AccessDeniedHandler;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;

import com.study.springboot.common.security.CustomAccessDeniedHandler;
import com.study.springboot.common.security.CustomUserDetailsService;
import com.study.springboot.filter.JwtAuthenticationFilter;
import com.study.springboot.filter.JwtAuthorizationFilter;


@Configuration         // 이 클래스를 빈으로 등록하는데 스프링 설정으로 사용
@EnableWebSecurity      // 이 클래스에 스프링 시큐리티 기능을 활성화
@EnableGlobalMethodSecurity(prePostEnabled=true, securedEnabled=true)
public class SecurityConfig extends WebSecurityConfigurerAdapter {
	
	@Autowired
	private DataSource dataSource;

   @Override
   protected void configure(HttpSecurity http) throws Exception {
      // url 에 대한 허용여부 설정
      // permitAll()             :     모두에게 접근 허용
      // hasRole(), hasAnyRole()   :   특정권한을 가진 사용자만 접근 허용      
//      http.authorizeRequests()
//            .antMatchers("/").permitAll()                        
//            .antMatchers("/css/**", "/js/**", "/img/**").permitAll()
//            .antMatchers("/guest/**").permitAll()
//            .antMatchers("/member/**").hasAnyRole("USER","AMDIN")
//            .antMatchers("/admin/**").hasRole("ADMIN")
//            .antMatchers("/**").permitAll()
//         .anyRequest().authenticated();
      
      
      // 로그인 페이지		: /loginForm
      // 로그인 에러 페이지	: /loginError
//      http.formLogin()
//      		.loginPage("/user/loginForm")
//      		.loginProcessingUrl("/user/login")
//      		.failureUrl("/user/loginError")
//      		.usernameParameter("username")
//      		.passwordParameter("password")
//      		.permitAll();
      
//      http.logout()
//      		.logoutUrl("/user/logout")
//      		.logoutSuccessUrl("/")
//      		.permitAll();
      
      // SSL을 사용하지 않으면 true를 사용
      // http.csrf().disable();
      
      // jwt 토큰 필터
      http.cors()
		.and()
		.csrf().disable()
		.exceptionHandling()
		.accessDeniedHandler(accessDeniedHandler())
		.and()
		.addFilter(new JwtAuthenticationFilter(authenticationManager()))
		.addFilter(new JwtAuthorizationFilter(authenticationManager()))
		.sessionManagement()
		.sessionCreationPolicy(SessionCreationPolicy.STATELESS)
		;
      
      
      
      
   }

   /*
   @Autowired
   public void configureGlobal(AuthenticationManagerBuilder auth) throws Exception {
      // inMemory 방식으로 인증 사용자 등록
      // id : user   /  pw : 1234   / 권한 : USER
      // id : admin  /  pw : 1234   / 권한 : ADMIN
      auth.inMemoryAuthentication()
         .withUser("user").password(passwordEncoder().encode("1234")).roles("USER")
         .and()
         .withUser("admin").password(passwordEncoder().encode("1234")).roles("ADMIN");
         
   }
   */
   
   
   /*
   @Override
   protected void configure(AuthenticationManagerBuilder auth) throws Exception {
	   
	   String query1 = " SELECT user_email as username, user_pw as password, 1 "
	   				 + " FROM membermomogo "
	   				 + " WHERE user_email = ? ";
	   
	   String query2 = " SELECT user_email as username, 'ROLE_USER' "
			   		 + " FROM membermomogo "
			   		 + " WHERE user_email = ? ";
	   
	   
	   // jdbc 방식으로 인증
	   auth.jdbcAuthentication()
	   	   .dataSource(dataSource)
	   	   .usersByUsernameQuery(query1)
	   	   .authoritiesByUsernameQuery(query2)
	   	   .passwordEncoder(new BCryptPasswordEncoder());
	   	   
	   
   }   
   */
   
   @Bean
	public UserDetailsService createUserDetailsService() {
		return new CustomUserDetailsService();
	}
	
	@Bean
	public PasswordEncoder createPasswordEncoder() {
		return new BCryptPasswordEncoder();
	}
	
	@Override
	protected void configure(AuthenticationManagerBuilder auth) throws Exception {
		auth.userDetailsService(createUserDetailsService())
		.passwordEncoder(createPasswordEncoder());
	}
	
	@Bean
	public CorsConfigurationSource corsConfigurationSource() {
		final UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
		source.registerCorsConfiguration("/**", new CorsConfiguration().applyPermitDefaultValues());

		return source;
	}
   
   // 접근 거부 처리자
   @Bean
	public AccessDeniedHandler accessDeniedHandler(){
		return new CustomAccessDeniedHandler();
	}

}