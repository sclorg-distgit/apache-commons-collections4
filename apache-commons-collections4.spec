%{?scl:%scl_package apache-commons-collections4}
%{!?scl:%global pkg_name %{name}}

Summary:        Extension of the Java Collections Framework
Name:           %{?scl_prefix}apache-commons-collections4
Version:        4.0
Release:        7.2%{?dist}
License:        ASL 2.0
URL:            http://commons.apache.org/proper/commons-collections/
BuildArch:      noarch

Source0:        http://www.apache.org/dist/commons/collections/source/commons-collections4-4.0-src.tar.gz

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(junit:junit)
BuildRequires:  %{?scl_prefix}mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.easymock:easymock)

%description
Commons-Collections seek to build upon the JDK classes by providing
new interfaces, implementations and utilities.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n commons-collections4-%{version}-src
%mvn_file : %{pkg_name} commons-collections4

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.txt RELEASE-NOTES.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Thu Jun 22 2017 Michael Simacek <msimacek@redhat.com> - 4.0-7.2
- Mass rebuild 2017-06-22

* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 4.0-7.1
- Automated package import and SCL-ization

* Tue Feb 07 2017 Michael Simacek <msimacek@redhat.com> - 4.0-7
- Regenerate buildrequires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 30 2015 Michael Simacek <msimacek@redhat.com> - 4.0-4
- Fix parent POM BR

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 4.0-2
- Use Requires: java-headless rebuild (#1067528)

* Mon Jan 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.0-1
- Initial packaging
