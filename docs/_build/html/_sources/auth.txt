.. _ref-auth:

================================
Auth
================================


Signin 회원가입
-----------------------

회원가입 API

URL: /accounts/signin/

Method: POST

.. note:: *기본적으로 모든 API는 POST로 처리한다*

.. note:: 비밀번호는 Client에서 암호화시켜서 전송해야함!

.. warning:: URL 마지막을 / 로 닫아줘야한다.

.. list-table:: Input Parameters
   :widths: 20 60
   :header-rows: 1

   * - var 
     - description
   * - opt
     - 1 : normal, 2 : facebook 로그인
   * - email
     - 이메일 (양식체크 미리 해주기 바람)
   * - password
     - 비밀번호 (암호화된 비밀번호를 보내기 바람)
   * - username
     - 사용자 이름
   * - gender
     - 성별 (1:남자, 2:여자)
   * - fb_id
     - 페이스북 id key값
   * - phone_num
     - 전화번호
   * - fb_friend
     - 페이스북 친구목록 (아직은 추가 안됨)


.. list-table:: Output
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - Status
     - 1 성공, 2 이메일 중복, 3 input값 없음, 4 옵션값체
   * - Log
     - 설명


Login
-----

로그인 API

URL : /accounts/login/


.. list-table:: Input Parameters
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - email
     - 이메일
   * - password
     - 비밀번호 (암호화된 비밀번호)


.. list-table:: Output
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - Status
     - 1 성공, 2 비밀번호 오류, 3 ID가 DB에 없음, 4 input값 없음
   * - Log
     - 설명
   * - Value
     - user의 id 값 (if success)



Logout
------

현재 API 불필요

