CELL_MK_DIR = $(PSL1GHT)/ppu_rules
include $(CELL_MK_DIR)

TARGET		:= ps3-cell-media.elf
BUILD		:= build
SOURCES		:= src
INCLUDES	:= include include/cjson

CFLAGS		= -O3 -Wall -ffast-math $(MACHDEP) $(INCLUDE)
CXXFLAGS	= $(CFLAGS)

LDFLAGS		= $(MACHDEP) -Wl,-Map,$(notdir $@).map -L$(PSL1GHT)/ppu/lib -L$(PSL1GHT)/portlibs/ppu/lib
LIBS		= -lcurl -lavformat -lavcodec -lavutil -lswscale -ltiny3d -lfont -lpng -lnet -lsysmodule -lsysutil -lio -lrsx -lgcm_sys -lm -lz -lssl -lpolarssl -llv2

INCLUDE		:= $(foreach dir,$(INCLUDES),-I$(dir)) \
			   -I$(PSL1GHT)/ppu/include -I$(PSL1GHT)/portlibs/ppu/include -I$(PSL1GHT)/ppu/include/tiny3d

CFILES		:= $(foreach dir,$(SOURCES),$(wildcard $(dir)/*.c))
CXXFILES	:= $(foreach dir,$(SOURCES),$(wildcard $(dir)/*.cpp))

OFILES		:= $(CFILES:%.c=$(BUILD)/%.o) $(CXXFILES:%.cpp=$(BUILD)/%.o)

all: $(TARGET)
	fself $(TARGET) $(TARGET:%.elf=%.self)

$(TARGET): $(OFILES)
	$(CC) $(LDFLAGS) $(OFILES) $(LIBS) -o $@

$(BUILD)/%.o: %.c
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) -c $< -o $@

$(BUILD)/%.o: %.cpp
	@mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) -c $< -o $@

pkg: $(TARGET:%.elf=%.self)
	npdrm package package.conf $(BUILD)
	python pkg.py

clean:
	rm -rf $(BUILD) $(TARGET) $(TARGET:%.elf=%.self) *.map *.pkg
