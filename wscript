#!/usr/bin/env python
# -*- encoding: utf-8 -*-

top = '.'
out = '.build'
prefix = 'out'

VERSION = '1.0.0'
APPNAME = 'uuid-mingw'


def options(opt):
	opt.add_option('--prefix', dest='prefix', default=prefix, help='installation prefix [default: %r]' % prefix)
	opt.load('compiler_c')


def configure(conf):
	conf.env.CC = 'x86_64-w64-mingw32-gcc'
	conf.env.AR = 'x86_64-w64-mingw32-ar'
	conf.load('compiler_c')


def build(bld):
	name='uuid'
	
	if bld.env.DEST_OS == 'win32':
		target='libuuid-1'
	else:
		target=name

	bld.shlib(
		name=name,
		target=target,
		source=bld.path.ant_glob('src/*.c'),
		includes=['./src', './include'],
		export_includes=['./include'],
		lib=['rpcrt4']
	)
	bld.program(
		target='test_uuid', 
		source=['test/test_uuid.c'],
		use=['uuid']
	)
	bld.install_files('${PREFIX}/include/uuid', ['include/uuid/uuid.h'])
	
