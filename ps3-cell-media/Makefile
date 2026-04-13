include $(PSL1GHT)/ppu_rules

TARGET		:= ps3-cell-media
TITLE		:= PS3 Cell Media
APPID		:= CELLMEDIA

SRC_DIR		:= src
BUILD_DIR	:= build

CFILES		:= $(wildcard $(SRC_DIR)/*.c)
CXXFILES	:= $(wildcard $(SRC_DIR)/*.cpp)
OFILES		:= $(CFILES:$(SRC_DIR)/%.c=$(BUILD_DIR)/%.o) $(CXXFILES:$(SRC_DIR)/%.cpp=$(BUILD_DIR)/%.o)

CFLAGS		+= -I$(PS3DEV)/portlibs/ppu/include -I$(PS3DEV)/ppu/include -O3 -Wall -ffast-math -Iinclude -Iinclude/cjson $(shell sdl2-config --cflags)
CXXFLAGS	+= $(CFLAGS)
LDFLAGS		+= -L$(PS3DEV)/portlibs/ppu/lib $(shell sdl2-config --libs) -lrsx -lsysutil -lio -laudio -lz -lm -lnet -llv2 -lcurl -lcJSON -lavcodec -lavformat -lswscale -lavutil

all: $(BUILD_DIR) $(TARGET).pkg

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c
	$(CC) $(CFLAGS) -c $< -o $@

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

$(TARGET).elf: $(OFILES)
	$(CXX) $(OFILES) $(LDFLAGS) -o $@

$(TARGET).self: $(TARGET).elf
	make_self $< $@

$(TARGET).pkg: $(TARGET).self
	make_package --conf package.conf $< $@

clean:
	rm -rf $(BUILD_DIR) $(TARGET).elf $(TARGET).self $(TARGET).pkg