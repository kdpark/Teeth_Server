.. _ref-pick:

================================
Pick
================================

주선자와 소개팅 대상에 관련된 모듈


Main (main화면)
-----------------------

main 화면에 필요한 정보를 리턴

URL: /main/

Method: POST


.. list-table:: Input Parameters
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - user_id
     - 페북사용자는 사용자key, 나머지는 이메일주소



.. list-table:: Output
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - Status
     - 1 성공, 2 잘못된 유저, 3 친구 모자람, 4 오늘의 chance 모두 소모
   * - Log
     - 메세지
   * - Value
     - 3 오류 시, 현재 친구 수를 리턴한다. 현재 3명미만은 3 오류를 유발시키게 구현되어있다.
   * - arranger_now
     - 주선자 이름
   * - arranger_now_pic
     - 주선자 프로필 사진
   * - candidate_now
     - 후보자 이름
   * - candidate_now_pic
     - 후보자 프로필 사진
   * - candidate_num
     - 대기자 수


Pick candidate (후보자 선택)
-----------------------------

상대방을 선택

URL : /pick_candidate/


.. list-table:: Input Parameters
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - user_id
     - 페북사용자는 사용자key, 나머지는 이메일주소


.. list-table:: Output
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - Status
     - 1 성공, 2 잘못된 사용자
   * - candidate_phone
     - 후보자의 전화번호
   * - candidate_pic
     - 후보자 사진


New Cycle (새로운 상대방 찾기)
--------------------------------------

이 API를 날리면, 모든 사용자에게 새로운 상대방을 매칭시켜준다.
오후 10시 등, 정해진 시간에 날리면 됨.

URL : /new_cycle/

.. warning:: API 성공 시, 기존에 있던 상대방 후보자는 새로운 후보자로 대체된다.

.. list-table:: Input Parameters
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - adminid
     - 트렐로 참고 (admin과 같음)
   * - password
     - 트렐로 참고할 것. (admin)


.. list-table:: Output
   :widths: 20 60
   :header-rows: 1

   * - var
     - description
   * - Status
     - 1 성공, 2 잘못된 사용자

