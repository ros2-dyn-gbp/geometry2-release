%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-tf2-tools
Version:        0.25.5
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS tf2_tools package

License:        BSD
URL:            http://www.ros.org/wiki/tf2_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       graphviz
Requires:       python%{python3_pkgversion}-yaml
Requires:       ros-humble-rclpy
Requires:       ros-humble-tf2-msgs
Requires:       ros-humble-tf2-py
Requires:       ros-humble-tf2-ros-py
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
tf2_tools

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/humble"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Mon Nov 13 2023 Chris Lalancette <clalancette@openrobotics.org> - 0.25.5-1
- Autogenerated by Bloom

* Tue Sep 19 2023 Chris Lalancette <clalancette@openrobotics.org> - 0.25.4-1
- Autogenerated by Bloom

* Mon Jul 17 2023 Chris Lalancette <clalancette@openrobotics.org> - 0.25.3-1
- Autogenerated by Bloom

* Tue Jan 10 2023 Chris Lalancette <clalancette@openrobotics.org> - 0.25.2-1
- Autogenerated by Bloom

* Mon Aug 08 2022 Chris Lalancette <clalancette@openrobotics.org> - 0.25.1-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Chris Lalancette <clalancette@openrobotics.org> - 0.25.0-2
- Autogenerated by Bloom

* Tue Apr 05 2022 Chris Lalancette <clalancette@openrobotics.org> - 0.25.0-1
- Autogenerated by Bloom

* Thu Mar 31 2022 Chris Lalancette <clalancette@openrobotics.org> - 0.24.0-1
- Autogenerated by Bloom

* Mon Mar 28 2022 Chris Lalancette <clalancette@openrobotics.org> - 0.23.0-1
- Autogenerated by Bloom

* Tue Mar 01 2022 Chris Lalancette <clalancette@openrobotics.org> - 0.22.0-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Chris Lalancette <clalancette@openrobotics.org> - 0.21.0-2
- Autogenerated by Bloom

