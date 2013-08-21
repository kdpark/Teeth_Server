.. _ref-auth:

================================
Auth
================================


Signin 회원가입
-----------------------

회원가입 API
opt1 은 소개슈머 자체 가입, opt2는 페북을 이용한 가입.

회원 가입 시 phone_contact, fb_friend를 POST로 보내주면
자동으로 친구목록이 동기화된다.

URL: /accounts/signin/

Method: POST

.. note:: *기본적으로 모든 API는 POST로 처리한다*

.. note:: 비밀번호는 Client에서 암호화시켜서 전송해야함!

.. warning:: URL 마지막을 / 로 닫아줘야한다.

.. list-table:: Input Parameters (option 1)
   :widths: 20 60
   :header-rows: 1

   * - var 
     - description
   * - opt
     - 1 : normal Login (using email)
   * - email
     - 이메일 (양식체크 미리 해주기 바람)
   * - password
     - 비밀번호 (암호화된 비밀번호를 보내기 바람)
   * - username
     - 사용자 이름
   * - gender
     - 성별 (1:남자, 2:여자)
   * - phone_num
     - 사용자의 전화번호
   * - phone_contact
     - 전화번호 주소록 목록 (csv형식, 공백없이!!) (ex: 01031311112,01094817411)


.. list-table:: Input Parameters (Option 2)
   :widths: 20 60
   :header-rows: 1

   * - var 
     - description
   * - opt
     - 2 : Facebook
   * - fb_id
     - 페이스북 key id (ex: 100001719640411)
   * - fb_email
     - 페이스북 이메일 주소
   * - username
     - 사용자 이름
   * - gender
     - 성별 (1:남자, 2:여자)
   * - phone_num
     - 전화번호
   * - phone_contact
     - 전화번호 주소록 목록 (csv형식, 공백없이!!)
   * - fb_friend
     - 페이스북 친구목록 (역시 csv 형식) (ex: 10014121411,4112515155,125166611)


.. list-table:: Output
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - Status
     - 1 성공, 2 이메일 중복, 3 input값 오류, 4 옵션값확인(1 or 2)
   * - Log
     - 설명


Login
-----

로그인 API
페이스북은 이 절차 필요없이 페북 로그인만 성공한 후 바로 main으로 이동하면 된다.

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

