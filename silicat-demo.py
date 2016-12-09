from pvlib import PvLib

if __name__ == "__main__":
    #dll = cdll.LoadLibrary("./libPvAPI.so")
    #ret = dll.PvInitialize()
    #if ret != 0:
        #print "initialization failed"
    #caminfo = tPvCameraInfo()
    #count = dll.PvCameraList(byref(caminfo), 1, None)
    #print count
    #print caminfo
    #dll.PvUnInitialize()
    print "\n!!!Starting test program for libpv!!!\n"
    pv = PvLib(verbose=True)
    cams = pv.getCameras()
    print "Camera List: ", cams
    if cams:
        cam = cams[0] 
        print "Using camera: ", cam
        cam.setAttr("Height", 1024)
        cam.setAttr("Width", 1360)
        #cam.setAttr("PacketSize", cam.getAttr("TotalBytesPerFrame")
        print "Setting optimal packet size for this network: ", cam.setOptimalPacketSize()
        cam.setAttr("GvspTimeout", 100)
        print "Image: "
        cam.printAttr("SensorWidth")
        cam.printAttr("SensorHeight")
        cam.printAttr("PixelFormat")
        cam.printAttr("Height")
        cam.printAttr("Width")
        print "Transport:"
        cam.printAttr("PacketSize")
        cam.printAttr("HeartBeatTimeout")
        cam.printAttr("TotalBytesPerFrame")
        cam.printAttr("GvspTimeout")
        cam.printAttr("GvspRetries")
        cam.printAttr("GvcpRetries")
        #cam.printAttr("GvspResentPercent")
        cam.printAttr("GvspSocketBuffersCount")
        cam.printAttr("BandwidthCtrlMode")
        cam.printAttr("StreamBytesPerSecond")
        cam.printAttr("TotalBytesPerFrame")
        print "Acquisition: "
        cam.printAttr("AcquisitionMode")
        cam.printAttr("FrameStartTriggerMode")
        cam.printAttr("FrameStartTriggerDelay")
        #cam.printAttr("FrameStartTriggerSoftware")
        #cam.printAttr("FrameStartTriggerEvent")
        #print "Stat"
        #cam.printAttr("StatFrameRate")
        #cam.printAttr("StatFramesCompleted")
        #cam.printAttr("StatFramesDropped")
        #cam.printAttr("StatFrameRate")
        if cam.opened:
            #cam.startCaptureTrigger()
            #frame = cam.getNumpyArray()
            #cam.stopCapture()
            from IPython.frontend.terminal.embed import InteractiveShellEmbed
            ipshell = InteractiveShellEmbed()
            ipshell(local_ns=locals())
        else:
            print "Camera is not opened"
    else:
        print "No camera found on network"



