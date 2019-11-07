import cooking #모듈

cooking.jjajang()
cooking.jambong()
cooking.pasta()
cooking.pizza()

from cooking import jjajang #한개만 가져와서 파일명 안쓰고 함수만 호출가능  

jjajang()

from cooking import* #전부다 가져올수있다

pasta()

from cookpackage import sex

sex.sex()
