# Install script for directory: /home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/diegopalma/Documents/ROSProjects/lab_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librbdl.so.2.6.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librbdl.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/build/librbdl.so.2.6.0"
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/build/librbdl.so"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librbdl.so.2.6.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/librbdl.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/rbdl" TYPE FILE FILES
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/include/rbdl/rbdl_mathutils.h"
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/include/rbdl/Model.h"
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/include/rbdl/Constraints.h"
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/include/rbdl/rbdl_eigenmath.h"
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/include/rbdl/SpatialAlgebraOperators.h"
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/include/rbdl/rbdl_math.h"
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/include/rbdl/Body.h"
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/include/rbdl/Dynamics.h"
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/include/rbdl/rbdl_utils.h"
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/include/rbdl/Kinematics.h"
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/include/rbdl/Quaternion.h"
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/include/rbdl/compileassert.h"
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/include/rbdl/Logging.h"
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/include/rbdl/Joint.h"
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/include/rbdl/rbdl.h"
    "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/build/include/rbdl/rbdl_config.h"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/build/rbdl.pc")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/build/addons/urdfreader/cmake_install.cmake")
  include("/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/build/python/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/diegopalma/Documents/ROSProjects/lab_ws/src/rbdl/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
