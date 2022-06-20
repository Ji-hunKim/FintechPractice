import React, { useState, useEffect } from 'react'
import HeaderWhite from '../components/HeaderWhite'
import { useLocation } from 'react-router-dom'  // 주소 객체 받아올 때 사용. react router dom의 hook (location에 대한 정보를 담고있는 hook, ?뒤에 있는 데이터 =쿼리스트링 받아올 수 있는 기능 담겨있음)
import queryString from 'query-string'
import axios from 'axios'

const AuthResult = () => {
    console.log(useLocation().search);  // 개발자 모드에서 object 확인 가능, object중에서 쿼리스트링만 -> .search
    //객체 구조분해할당 (쿼리스트링 중에서 code만 바로 가져올 수 있음)
    const { code } = queryString.parse(useLocation().search);
    console.log(code) // 쿼리 받아서 code
    const [accessToken, setaccessToken] = useState("토큰을 받기 전입니다.");
    const [userSeqNo, setuserSeqNo] = useState("사용자 번호");

    // 페이지 업데이트할때 , 최초 접속할때 사용하는 기능
    // 배열이[] 공백이라면 = 페이지 최초접속 이라면 해당 기능을 실행시키겟다는 의미
    useEffect(() => {
      getAccessToken();
    }, []);

    const getAccessToken = () => {
      const sendData = {
        code: code,
        client_id: "c137c686-fafa-44c4-870c-8f606409bc49",
        client_secret: "669e8093-0c39-455c-918d-c94bd24b6794",
        redirect_uri: "http://localhost:3000/authResult",
        grant_type: "authorization_code",
      };
      // object이렇게 보내면 api주소 서버에서는 parsing을 못하기 때문에 query string을 통해 urlencoded type으로 encoded
      const encodedData = queryString.stringify(sendData);
      //axios로 요청보내기
      const option = {
        method : "POST",
        url : "/oauth/2.0/token",
        headers : {
          "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        },
        data : encodedData,
      };
      //option을 보내서 data로 받는 형태
      axios(option).then(( {data} )=>{     //axios요청 보낼 때 url이 아니라 option을 따로 뽑아서 보낼 수도 있음
        console.log(data);
        // 에러메세지 샘플
        if (data.rsp_code === "O0001"){
          alert(data.rsp_message);
        } else{
          const accessToken = data.access_token;
          const userSeqNo = data.user_seq_no;
          setaccessToken(accessToken);
          setuserSeqNo(userSeqNo);
          localStorage.setItem("accessToken", data.access_token);
          localStorage.setItem("userSeqNo", data.user_seq_no)
        }
      });
    }
  return (

    // click버튼 누르면 함수 실행되고 해당 함수 결과값이 useState를 통해 변경되면서 화면에 렌더링되될 수 있도록
    <div>
        <HeaderWhite title={"AccessToken 요청"}></HeaderWhite>
        <p>인증코드: {code}</p>
        <p>AccessToken: {accessToken}</p>
        <p>사용자 번호: {userSeqNo}</p>
        <button onClick={getAccessToken}>토큰 요청</button>
    </div>
  )
}

export default AuthResult