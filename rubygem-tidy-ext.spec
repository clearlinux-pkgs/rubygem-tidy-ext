#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-tidy-ext
Version  : 0.1.14
Release  : 6
URL      : https://rubygems.org/downloads/tidy-ext-0.1.14.gem
Source0  : https://rubygems.org/downloads/tidy-ext-0.1.14.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : W3C
Requires: rubygem-tidy-ext-lib
BuildRequires : ruby
BuildRequires : rubygem-chronic_duration
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-numerizer
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-spec

%description
Description
-----------
This is the HTML Tidy library built as a Ruby extension.

%package lib
Summary: lib components for the rubygem-tidy-ext package.
Group: Libraries

%description lib
lib components for the rubygem-tidy-ext package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n tidy-ext-0.1.14
gem spec %{SOURCE0} -l --ruby > rubygem-tidy-ext.gemspec

%build
gem build rubygem-tidy-ext.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
tidy-ext-0.1.14.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/tidy-ext-0.1.14
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/tidy-ext-0.1.14.gem
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/tidy-ext-0.1.14/gem.build_complete
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/tidy-ext-0.1.14/gem_make.out
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/README.md
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/VERSION
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/.RUBYARCHDIR.time
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/Makefile
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/access.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/access.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/access.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/alloc.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/alloc.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/attrask.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/attrask.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/attrdict.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/attrdict.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/attrdict.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/attrget.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/attrget.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/attrs.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/attrs.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/attrs.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/buffio.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/buffio.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/buffio.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/charsets.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/charsets.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/charsets.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/clean.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/clean.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/clean.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/config.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/config.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/config.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/entities.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/entities.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/entities.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/extconf.rb
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/fileio.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/fileio.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/fileio.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/forward.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/iconvtc.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/iconvtc.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/iconvtc.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/istack.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/istack.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/lexer.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/lexer.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/lexer.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/localize.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/localize.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/mappedio.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/mappedio.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/mappedio.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/message.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/parser.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/parser.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/parser.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/platform.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/pprint.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/pprint.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/pprint.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/ruby-tidy.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/ruby-tidy.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/streamio.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/streamio.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/streamio.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/tagask.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/tagask.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/tags.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/tags.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/tags.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/tidy-int.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/tidy.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/tidyenum.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/tidylib.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/tidylib.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/tmbstr.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/tmbstr.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/tmbstr.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/utf8.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/utf8.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/utf8.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/version.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/win32tc.c
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/win32tc.h
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/win32tc.o
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/features/step_definitions/tidy_steps.rb
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/spec/tidy/compat_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/spec/tidy/remote_uri_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/spec/tidy/test1.html
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/spec/tidy/tidy_spec.rb
/usr/lib64/ruby/gems/2.3.0/specifications/tidy-ext-0.1.14.gemspec

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/tidy-ext-0.1.14/tidy.so
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/ext/tidy/tidy.so
/usr/lib64/ruby/gems/2.3.0/gems/tidy-ext-0.1.14/lib/tidy.so
