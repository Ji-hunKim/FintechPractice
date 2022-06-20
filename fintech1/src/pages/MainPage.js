import axios from 'axios';
import React, { useState, useEffect } from 'react'
import HeaderWhite from '../components/HeaderWhite'
import MainCard from '../components/Main/MainCard';

const MainPage = () => {
    useEffect(() => {
        getAccountList();
    }, []);

    const [accountList, setaccountList] = useState([]);
    // 로컬스토리지에 토큰 저장했기 때문에 사용자 정보조회 API 요청 보내야함
    // 헤더에 토큰을 집어넣어야하고 파라미터에 use seq no 넣어야함
    // = 즉 local storage에 저장된 데이터값을 불러와야함
    const getAccountList = () => {
        const accessToken = localStorage.getItem("accessToken");
        const userSeqNo = localStorage.getItem("userSeqNo");
    

        const sendData = {
            user_seq_no: userSeqNo
        };

        // work7 사용자 정보 조회 API를 통해 accountList에 계좌 목록을 저장
        // 1. axios 요청 작성
        // get방식 : url 데이터 자정 / data 항목 대신 params 라는 항목 사용가능
        // 2. setaccountList 실행
        const option = {
            method : "GET",
            url : "/v2.0/user/me",
            headers : {
                Authorization: `Bearer ${accessToken}`
            },
            params : sendData,
        };

        axios(option).then(({ data }) => {
            const accountListsFromRequest = data.res_list;
            setaccountList(accountListsFromRequest);
            //setaccountList()
        })

    }
  return (
    <div>
        <HeaderWhite title={"메인페이지(계좌목록)"}></HeaderWhite>
        {accountList.map(( {fintech_use_num, bank_name} ) => {
            return (
            <MainCard bankName={bank_name} fintechUseNo={fintech_use_num}></MainCard>
            )
        })}
    </div>
  )
}

export default MainPage