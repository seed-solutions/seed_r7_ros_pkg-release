%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/melodic/.*$
%global __requires_exclude_from ^/opt/ros/melodic/.*$

Name:           ros-melodic-seed-r7-typef-moveit-config
Version:        0.3.3
Release:        1%{?dist}
Summary:        ROS seed_r7_typef_moveit_config package

License:        BSD
URL:            http://moveit.ros.org/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-joint-state-publisher
Requires:       ros-melodic-moveit-fake-controller-manager
Requires:       ros-melodic-moveit-kinematics
Requires:       ros-melodic-moveit-planners-ompl
Requires:       ros-melodic-moveit-ros-move-group
Requires:       ros-melodic-moveit-ros-visualization
Requires:       ros-melodic-moveit-setup-assistant
Requires:       ros-melodic-robot-state-publisher
Requires:       ros-melodic-rviz
Requires:       ros-melodic-seed-r7-description
Requires:       ros-melodic-tf
Requires:       ros-melodic-xacro
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-seed-r7-description

%description
An automatically generated package with all the configuration and launch files
for using the SEED-Noid-Mover-typeF with the MoveIt! Motion Planning Framework

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/melodic

%changelog
* Wed Dec 04 2019 Yasuto Shiigi <y.shiigi@thk.co.jp> - 0.3.3-1
- Autogenerated by Bloom

