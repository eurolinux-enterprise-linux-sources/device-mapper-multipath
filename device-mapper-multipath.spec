Summary: Tools to manage multipath devices using device-mapper
Name: device-mapper-multipath
Version: 0.4.9
Release: 100%{?dist}
License: GPL+
Group: System Environment/Base
URL: http://christophe.varoqui.free.fr/

Source0: multipath-tools-091027.tar.gz
Source1: multipath.conf
# patch that should go upstream
Patch1: 0001-for-upstream-add-tpg_pref-prioritizer.patch
Patch2: 0002-for-upstream-add-tmo-config-options.patch
Patch3: 0003-for-upstream-default-configs.patch
# local patches
Patch1001: 0001-RH-queue-without-daemon.patch
Patch1002: 0002-RH-path-checker.patch
Patch1003: 0003-RH-root-init-script.patch
Patch1004: 0004-RH-fix-kpartx.patch
Patch1005: 0005-RH-cciss_id.patch
Patch1006: 0006-RH-move-bindings.patch
Patch1007: 0007-RH-do-not-remove.patch
Patch1008: 0008-RH-Make-build-system-RH-Fedora-friendly.patch
Patch1009: 0009-RH-multipathd-blacklist-all-by-default.patch
Patch1010: 0010-RH-multipath-rules-udev-changes.patch
Patch1011: 0011-RH-fix-init-script-LSB-headers.patch
Patch1012: 0012-RH-udev-sync-support.patch
Patch1013: 0013-RH-add-weighted_prio-prioritizer.patch
Patch1014: 0014-RH-add-hp_tur-checker.patch
Patch1015: 0015-RH-add-multipathd-count-paths-cmd.patch
Patch1016: 0016-RHBZ-554561-fix-init-error-msg.patch
Patch1017: 0017-RHBZ-554592-man-page-note.patch
Patch1018: 0018-RHBZ-554596-SUN-6540-config.patch
Patch1019: 0019-RHBZ-554598-fix-multipath-locking.patch
Patch1020: 0020-RHBZ-554605-fix-manual-failover.patch
Patch1021: 0021-RHBZ-558636-add-find-multipaths.patch
Patch1022: 0022-RHBZ-557845-RHEL5-style-partitions.patch
Patch1023: 0023-RHBZ-557810-emc-invista-config.patch
Patch1024: 0024-RHBZ-565933-checker-timeout.patch
Patch1025: 0025-RHBZ-508827-update-multipathd-manpage.patch
Patch1026: 0026-RHBZ-549636-default-path-selector.patch
Patch1027: 0027-RHBZ-509443-enhance-show-config.patch
Patch1028: 0028-RHBZ-452617-add-revision-parameter.patch
Patch1029: 0029-RHBZ-567219-recalculate-pgs-in-checkerloop.patch
Patch1030: 0030-RHBZ-558636-check-if-multipath-owns-path.patch
Patch1031: 0031-RHBZ-570546-display-avg-pg-prio.patch
Patch1032: 0032-RHBZ-575767-ontap_prio.patch
Patch1033: 0033-RHBZ-573715-eurologic-config.patch
Patch1034: 0034-RHBZ-579575-add-q-multipath-option.patch
Patch1035: 0035-RHBZ-467709-add-followover.patch
Patch1036: 0036-RH-clear-messages.patch
Patch1037: 0037-RH-adopt-paths.patch
Patch1038: 0038-RHBZ-587201-IBM-SGI.patch
Patch1039: 0039-RHBZ-589153-manpage-update.patch
Patch1040: 0040-RHBZ-587695-add-checker-msg-alias.patch
Patch1041: 0041-RHBZ-587695-add-rdac-message.patch
Patch1042: 0042-RHBZ-590038-fix-fast-io-fail-tmo.patch
Patch1043: 0043-RHBZ-590028-close-sysfs_attr_fd.patch
Patch1044: 0044-RHBZ-591940-dont-clear-daemon.patch
Patch1045: 0045-RHBZ-593379-dont-add-unknown-paths.patch
Patch1046: 0046-RHBZ-593426-move-adopt-path.patch
Patch1047: 0047-RHBZ-591608-only-switch-pgs-once.patch
Patch1048: 0048-RHBZ-592494-fix-user-configs.patch
Patch1049: 0049-RHBZ-591644-enhance-mpathconf.patch
Patch1050: 0050-RHBZ-595400-fix-checker-tmo.patch
Patch1051: 0051-RHBZ-596156-mpathconf-man-page.patch
Patch1052: 0052-RHBZ-601247-fix-path-adoption.patch
Patch1053: 0053-RHBZ-596323-remember_more_wwids.patch
Patch1054: 0054-RHBZ-596319-rules-cleanup.patch
Patch1055: 0055-RHBZ-602257-update-on-show-topology.patch
Patch1056: 0056-RHBZ-603812-better-type-check.patch
Patch1057: 0057-RHBZ-607869-fix-resize.patch
Patch1058: 0058-RHBZ-601665-assemble-features.patch
Patch1059: 0059-RHBZ-607874-handle-offlined-paths.patch
Patch1060: 0060-RHBZ-606420-fix-remove-map.patch
Patch1061: 0061-RHBZ-620479-find-rport.patch
Patch1062: 0062-RHBZ-592998-hpsc-config.patch
Patch1063: 0063-RHBZ-595719-udev_link_priority.patch
Patch1064: 0064-RHBZ-612173-fix-reverse-lookup.patch
Patch1065: 0065-RHBZ-635088-update-priority.patch
Patch1066: 0066-RHBZ-636071-mpathconf-variable_names.patch
Patch1067: 0067-RHBZ-622569-symmetrix-config.patch
Patch1068: 0068-RHBZ-632734-nvdisk-config.patch
Patch1069: 0069-RHBZ-636246-hp-open-config.patch
Patch1070: 0070-RHBZ-639037-hitachi-open-config.patch
Patch1071: 0071-RHBZ-611779-fix-whitespace-crash.patch
Patch1072: 0072-RHBZ-651389-change-scsi-tmo-order.patch
Patch1073: 0073-RHBZ-650664-clarify-error-msg.patch
Patch1074: 0074-RHBZ-602883-dont-print-change.patch
Patch1075: 0075-RHBZ-576919-log-checker-err.patch
Patch1076: 0076-RHBZ-599690-update-multipath-conf.patch
Patch1077: 0077-RHBZ-622608-nvdisk-config.patch
Patch1078: 0078-RHBZ-628095-config-warnings.patch
Patch1079: 0079-RHBZ-650797-display-iscsi-tgt-name.patch
Patch1080: 0080-RHBZ-662731-fix-no-config-value-segfault.patch
Patch1081: 0081-RHBZ-623644-fix-sysfs-caching.patch
Patch1083: 0083-RHBZ-636213-633643-new-configs.patch
Patch1084: 0084-RHBZ-644111-read-only-bindings.patch
Patch1085: 0085-RHBZ-645605-fix-offline-check.patch
Patch1086: 0086-RHBZ-681144-sysfs-device-cleanup.patch
Patch1087: 0087-RHBZ-680480-skip-if-no-sysdev.patch
Patch1088: 0088-RHBZ-693524-fix-prio-segfault.patch
Patch1089: 0089-RHBZ-694602-RSSM-config.patch
Patch1090: 0090-RHBZ-700169-fix-nr-active.patch
Patch1091: 0091-RHBZ-699577-manpage-clarification.patch
Patch1092: 0092-RHBZ-689504-rdac-retry.patch
Patch1093: 0093-RHBZ-677449-dont-remove-map-on-enomem.patch
Patch1094: 0094-RHBZ-707560-check-return-value.patch
Patch1095: 0095-RHBZ-678673-no-path-groups.patch
Patch1096: 0096-RHBZ-683616-ioship-support.patch
Patch1097: 0097-RHBZ-697386-fix-shutdown-crash.patch
Patch1098: 0098-RHBZ-706555-dont-update-pgs-in-manual.patch
Patch1099: 0099-RHBZ-705854-warn-on-bad-dev-loss-tmo.patch
Patch1100: 0100-RHBZ-710478-deprecate-uid-gid-mode.patch
Patch1101: 0101-RHBZ-631009-disable-udev-disk-rules-on-reload.patch
Patch1102: 0102-RHBZ-714821-dont-remove-map-twice.patch
Patch1103: 0103-RHBZ-725541-09-no-partitions.patch
Patch1104: 0104-RHBZ-725541-10-force-devmap.patch
Patch1105: 0105-RHBZ-725541-08-reset-running.patch
Patch1106: 0106-RHBZ-725541-07-tur-checker-reservation-conflict.patch
Patch1107: 0107-RHBZ-725541-01-async-tur-checker.patch
Patch1108: 0108-RHBZ-725541-06-offline-check.patch
Patch1109: 0109-RHBZ-725541-05-only-count-up-and-ghost-paths.patch
Patch1110: 0110-RHBZ-725541-04-serialize-startup.patch
Patch1111: 0111-RHBZ-725541-03-handle-LBA_DEPENDENT-state.patch
Patch1112: 0112-RHBZ-725541-02-infinite-dev-loss-tmo.patch
Patch1113: 0113-RHBZ-719571-validate-guid-partitions.patch
Patch1114: 0114-RHBZ-723168-adjust-messages.patch
Patch1115: 0115-RHBZ-713754-lower-minio.patch
Patch1116: 0116-RH-manpage-update.patch
Patch1117: 0117-RHBZ-697386-logger-shutdown-crash.patch
Patch1118: 0118-RHBZ-738298-revert-631009.patch
Patch1119: 0119-RHBZ-747604-fix-async-tur.patch
Patch1120: 0120-RHBZ-752989-tighten_vendor_product_regex.patch
Patch1121: 0121-RHBZ-751938-fix-usage-return.patch
Patch1122: 0122-RHBZ-750132-fix-oom-adj.patch
Patch1123: 0123-RHBZ-732932-fix-coverity-issues.patch
Patch1124: 0124-RHBZ-751039-fix-shutdown.patch
Patch1125: 0125-RHBZ-727429-dont-print-exec-fails.patch
Patch1126: 0126-RHBZ-740760-kpartx-man-page.patch
Patch1127: 0127-RHBZ-737051-add-netapp-brand.patch
Patch1128: 0128-RHBZ-796384-fix-alua.patch
Patch1129: 0129-RHBZ-788963-eternus-config.patch
Patch1130: 0130-RHBZ-754586-use-sync-support.patch
Patch1131: 0131-RHBZ-662433-override-queue-no-daemon.patch
Patch1132: 0132-RHBZ-744756-regex-hw-match.patch
Patch1133: 0133-RHBZ-744210-config-changes.patch
Patch1134: 0134-RHBZ-769527-fix-flush-on-last-del.patch
Patch1135: 0135-RHBZ-798541-build-options.patch
Patch1136: 0136-RHBZ-799908-ibm-xiv.patch
Patch1137: 0137-RHBZ-799842-change-netapp-config.patch
Patch1138: 0138-RH-fix-strings.patch
Patch1139: 0139-RHBZ-800288-netapp-devloss.patch
Patch1140: 0140-RHBZ-803527-blacklist-management-luns.patch
Patch1141: 0141-RHBZ-752989-remove-dup-configs.patch
Patch1142: 0142-RHBZ-769527-fix-features-build.patch
Patch1143: 0143-RHBZ-467709-followover-chkr-state.patch
Patch1144: 0144-RHBZ-812832-shutdown-crash.patch
Patch1145: 0145-RHBZ-831045-realloc-vector.patch
Patch1146: 0146-RHBZ-595692-fix-cciss-names.patch
Patch1147: 0147-RHBZ-824243-826610-833124-doc-fix.patch
Patch1148: 0148-RHBZ-619173-storagetek-config.patch
Patch1149: 0149-RHBZ-810788-remove-dups.patch
Patch1150: 0150-RHBZ-810755-update-conf-defaults.patch
Patch1151: 0151-RHBZ-822389-fix-rename.patch
Patch1152: 0152-RHBZ-735459-mpath_persist.patch
Patch1153: 0153-RHBZ-839386-retain_hwhandler.patch
Patch1154: 0154-RHBZ-578114-kpartx-retry.patch
Patch1155: 0155-RHBZ-810989-load-modules.patch
Patch1156: 0156-RHBZ-813963-new-alua-prio.patch
Patch1157: 0157-RHBZ-816717-flush-full-paths.patch
Patch1158: 0158-RHBZ-821885-check-blacklist.patch
Patch1159: 0159-RHBZ-818367-829065-rdac.patch
Patch1160: 0160-RHBZ-841732-dont-swap-devices.patch
Patch1161: 0161-RHBZ-836890-AIX-whitespace.patch
Patch1162: 0162-RHBZ-860748-early-blacklist.patch
Patch1163: 0163-RHBZ-839386-detect-prio.patch
Patch1164: 0164-RHBZ-839386-netapp-config.patch
Patch1165: 0165-RHBZ-869253-disable-libdm-failback.patch
Patch1166: 0166-RHBZ-880487-make-path-fd-readonly.patch
Patch1167: 0167-RHBZ-735459-fix-mpathpersist-fns.patch
Patch1168: 0168-RHBZ-902585-fix-state-size.patch
Patch1169: 0169-RHBZ-895110-fix-params-size.patch
Patch1170: 0170-RHBZ-889441-fix-multipath.rules.patch
Patch1171: 0171-RHBZ-904836-handle-other-sector-sizes.patch
Patch1172: 0172-RHBZ-895110-fix-output-buffer.patch
Patch1173: 0173-RHBZ-889429-catch-early-uevents.patch
Patch1174: 0174-RHBZ-875199-null-vector-fix.patch
Patch1175: 0175-RHBZ-889987-detect_prio_fix.patch
Patch1176: 0176-RHBZ-892292-listing-speedup.patch
Patch1177: 0177-RHBZ-902593-multipath-c-manpage.patch
Patch1178: 0178-RHBZ-918825-kpartx-loop-devices.patch
Patch1179: 0179-RHBZ-920448-bindings-fix.patch
Patch1180: 0180-RHBZ-928831-check-dm-version-for-retain_hwhandler.patch
Patch1181: 0181-RHBZ-958091-check-for-erofs.patch
Patch1182: 0182-RHBZ-947798-rw-change.patch
Patch1183: 0183-RHBZ-924924-replace_whitespace.patch
Patch1184: 0184-RHBZ-975676-fix_cli_resize.patch
Patch1185: 0185-RH-signal-waiter.patch
Patch1186: 0186-RHBZ-974129-delay_set_fast_io_fail.patch
Patch1187: 0187-RH-fix-bad-derefs.patch
Patch1188: 0188-RH-add-all_devs.patch
Patch1189: 0189-RHBZ-986767-blacklist-td-devs.patch
Patch1190: 0190-UPBZ-994277-handle-offline-states.patch
Patch1191: 0191-UPBZ-995251-fail-rdac-on-unavailable.patch
Patch1192: 0192-RHBZ-916667-print-major-minor.patch
Patch1193: 0193-UPBZ-1011341-dos-4k-partition-fix.patch
Patch1194: 0194-RHBZ-997570-no-sync-turs-on-pthread_cancel.patch
Patch1195: 0195-UPBZ-1024103-alua-prio-timeout.patch
Patch1196: 0196-RHBZ-1012672-fix-sysdev.patch
Patch1197: 0197-RHBZ-1049315-netapp-rw-change.patch
Patch1198: 0198-RHBZ-1080052-orphan-paths-on-reload.patch
Patch1199: 0199-RHBZ-1007719-multipath-man.patch
Patch1200: 0200-RHBZ-1009061-allow_devt.patch
Patch1201: 0201-RHBZ-1018697-cli-use-basename.patch
Patch1202: 0202-RHBZ-1024604-weighted-prio-man.patch
Patch1203: 0203-RHBZ-1054046-mpathconf-typo.patch
Patch1204: 0204-RHBZ-1067102-doc-add-selectors.patch
Patch1205: 0205-RHBZ-1072974-alua-typo.patch
Patch1206: 0206-UPBZ-1020556-e-series-config.patch
Patch1207: 0207-UPBZ-1027061-sg-read-use-buffsize.patch
Patch1208: 0208-UPBZ-1028220-datacore-config.patch
Patch1209: 0209-RHBZ-999766-update-annotated.patch
Patch1210: 0210-UPBZ-1099932-fast-io-fail-iscsi.patch
Patch1211: 0211-UPBZ-1088013-reorder-paths-for-round-robin.patch
Patch1212: 0212-RHBZ-1086417-orphan-path-on_failed-add.patch
Patch1213: 0213-RHBZ-1069641-config-error-checking.patch
Patch1214: 0214-RHBZ-1078485-configurable-prio-timeout.patch
Patch1215: 0215-RHBZ-1054747-add-noasync-option.patch
Patch1216: 0216-RHBZ-1095868-multipathd-man-typo.patch
Patch1217: 0217-RHBZ-1101101-add-w-options.patch
Patch1218: 0218-RHBZ-1117714-configure-missing-devs.patch
Patch1219: 0219-RHBZ-1136966-fix-partition-mapping-creation-race-with-kpartx.patch
Patch1220: 0220-RHBZ-1128786-dont-show-pg-timeout.patch
Patch1221: 0221-RHBZ-1175888-add-wwid-option.patch
Patch1222: 0222-RHBZ-1175888-cmdline-wwid.patch
Patch1223: 0223-UPBZ-1120047-change-alua-prio.patch
Patch1224: 0224-UPBZ-1148096-reload-on-rename.patch
Patch1225: 0225-UPBZ-1148096-user-friendly-name-remap.patch
Patch1226: 0226-RHBZ-1006895-add-config_dir-option.patch
Patch1227: 0227-RHBZ-1171862-thread-safe.patch
Patch1228: 0228-RHBZ-1072081-delayed-reintegration.patch
Patch1229: 0229-UPBZ-1168987-queue_if_no_path_issue.patch
Patch1230: 0230-RHBZ-880121-fix-double-free.patch
Patch1231: 0231-RHBZ-978947-dell-36xxi.patch
Patch1232: 0232-RHBZ-997028-autodetect-clariion-alua.patch
Patch1233: 0233-RHBZ-1215903-remove-pg-timeout.patch
Patch1234: 0234-RHBZ-818404-update-doc.patch
Patch1235: 0235-RHBZ-1033789-rdac-update.patch
Patch1236: 0236-RH-per-path-prio.patch
Patch1237: 0237-RHBZ-1081395-save-alua-info.patch
Patch1238: 0238-RHBZ-1153704-async-timeout.patch
Patch1239: 0239-RHBZ-1201444-update-eternus-config.patch
Patch1241: 0241-RHBZ-1214127-fix-help.patch
Patch1242: 0242-RHBZ-1238507-kpartx-fix.patch
Patch1243: 0243-RHBZ-1248177-reset-alias.patch
Patch1244: 0244-RHBZ-1254692-kpartx-sync.patch
Patch1245: 0245-RHBZ-1273829-autodetect-readonly-devs.patch
Patch1246: 0246-RHBZ-1145442-raw-output-and-wildcards.patch
Patch1247: 0247-RHBZ-1283181-fix-remove-crash.patch
Patch1248: 0248-RHBZ-1289353-alua-pref-arg.patch
Patch1249: 0249-RHBZ-1208521-fix-typo-configure.patch
Patch1250: 0250-RHBZ-1316165-fix-i686-size-bug.patch
Patch1251: 0251-RHBZ-1349376-fix-makefile.patch
Patch1252: 0252-RHBZ-1333334-huawei-config.patch
Patch1253: 0253-RHBZ-1305589-check-multipathd.patch
Patch1254: 0254-RHBZ-1310320-no-kpartx.patch
Patch1255: 0255-UPBZ-1322532-disable-reinstate.patch
Patch1256: 0256-RHBZ-1324764-man-page-typo.patch
Patch1257: 0257-UPBZ-1328077-resize-map.patch
Patch1258: 0258-UPBZ-1300414-PURE_config.patch
Patch1259: 0259-UPBZ-1343747-dont-fail-discovery.patch
Patch1260: 0260-RHBZ-1364879-check-mpath-prefix.patch
Patch1261: 0261-RHBZ-1377532-disable-changed-paths.patch
Patch1262: 0262-RH-free-vector.patch
Patch1263: 0263-RHBZ-1365710-no-use-after-free.patch
Patch1264: 0264-RHBZ-1390472-dont-exit.patch
Patch1265: 0265-RHBZ-1355669-max-sectors-kb.patch
Patch1266: 0266-RHBZ-1401391-fix-prio-put.patch
Patch1267: 0267-RHBZ-1401769-orphan-status.patch


# runtime
Requires: %{name}-libs = %{version}-%{release}
Requires: kpartx = %{version}-%{release}
Requires: device-mapper >= 1.02.117-10.el6
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
Requires(postun): initscripts

# build/setup
BuildRequires: libaio-devel, device-mapper-devel >= 1.02.89
BuildRequires: libselinux-devel, libsepol-devel
BuildRequires: readline-devel, ncurses-devel

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
%{name} provides tools to manage multipath devices by
instructing the device-mapper multipath kernel module what to do. 
The tools are :
* multipath - Scan the system for multipath devices and assemble them.
* multipathd - Detects when paths fail and execs multipath to update things.

%package libs
Summary: The %{name} modules and shared library
License: GPL+
Group: System Environment/Libraries

%description libs
The %{name}-libs provides the path checker
and prioritizer modules. It also contains the multipath shared library,
libmultipath.

%package -n kpartx
Summary: Partition device manager for device-mapper devices
Group: System Environment/Base

%description -n kpartx
kpartx manages partition creation and removal for device-mapper devices.

%prep
%setup -q -n multipath-tools
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%patch1005 -p1
%patch1006 -p1
%patch1007 -p1
%patch1008 -p1
%patch1009 -p1
%patch1010 -p1
%patch1011 -p1
%patch1012 -p1
%patch1013 -p1
%patch1014 -p1
%patch1015 -p1
%patch1016 -p1
%patch1017 -p1
%patch1018 -p1
%patch1019 -p1
%patch1020 -p1
%patch1021 -p1
%patch1022 -p1
%patch1023 -p1
%patch1024 -p1
%patch1025 -p1
%patch1026 -p1
%patch1027 -p1
%patch1028 -p1
%patch1029 -p1
%patch1030 -p1
%patch1031 -p1
%patch1032 -p1
%patch1033 -p1
%patch1034 -p1
%patch1035 -p1
%patch1036 -p1
%patch1037 -p1
%patch1038 -p1
%patch1039 -p1
%patch1040 -p1
%patch1041 -p1
%patch1042 -p1
%patch1043 -p1
%patch1044 -p1
%patch1045 -p1
%patch1046 -p1
%patch1047 -p1
%patch1048 -p1
%patch1049 -p1
%patch1050 -p1
%patch1051 -p1
%patch1052 -p1
%patch1053 -p1
%patch1054 -p1
%patch1055 -p1
%patch1056 -p1
%patch1057 -p1
%patch1058 -p1
%patch1059 -p1
%patch1060 -p1
%patch1061 -p1
%patch1062 -p1
%patch1063 -p1
%patch1064 -p1
%patch1065 -p1
%patch1066 -p1
%patch1067 -p1
%patch1068 -p1
%patch1069 -p1
%patch1070 -p1
%patch1071 -p1
%patch1072 -p1
%patch1073 -p1
%patch1074 -p1
%patch1075 -p1
%patch1076 -p1
%patch1077 -p1
%patch1078 -p1
%patch1079 -p1
%patch1080 -p1
%patch1081 -p1
%patch1083 -p1
%patch1084 -p1
%patch1085 -p1
%patch1086 -p1
%patch1087 -p1
%patch1088 -p1
%patch1089 -p1
%patch1090 -p1
%patch1091 -p1
%patch1092 -p1
%patch1093 -p1
%patch1094 -p1
%patch1095 -p1
%patch1096 -p1
%patch1097 -p1
%patch1098 -p1
%patch1099 -p1
%patch1100 -p1
%patch1101 -p1
%patch1102 -p1
%patch1103 -p1
%patch1104 -p1
%patch1105 -p1
%patch1106 -p1
%patch1107 -p1
%patch1108 -p1
%patch1109 -p1
%patch1110 -p1
%patch1111 -p1
%patch1112 -p1
%patch1113 -p1
%patch1114 -p1
%patch1115 -p1
%patch1116 -p1
%patch1117 -p1
%patch1118 -p1
%patch1119 -p1
%patch1120 -p1
%patch1121 -p1
%patch1122 -p1
%patch1123 -p1
%patch1124 -p1
%patch1125 -p1
%patch1126 -p1
%patch1127 -p1
%patch1128 -p1
%patch1129 -p1
%patch1130 -p1
%patch1131 -p1
%patch1132 -p1
%patch1133 -p1
%patch1134 -p1
%patch1135 -p1
%patch1136 -p1
%patch1137 -p1
%patch1138 -p1
%patch1139 -p1
%patch1140 -p1
%patch1141 -p1
%patch1142 -p1
%patch1143 -p1
%patch1144 -p1
%patch1145 -p1
%patch1146 -p1
%patch1147 -p1
%patch1148 -p1
%patch1149 -p1
%patch1150 -p1
%patch1151 -p1
%patch1152 -p1
%patch1153 -p1
%patch1154 -p1
%patch1155 -p1
%patch1156 -p1
%patch1157 -p1
%patch1158 -p1
%patch1159 -p1
%patch1160 -p1
%patch1161 -p1
%patch1162 -p1
%patch1163 -p1
%patch1164 -p1
%patch1165 -p1
%patch1166 -p1
%patch1167 -p1
%patch1168 -p1
%patch1169 -p1
%patch1170 -p1
%patch1171 -p1
%patch1172 -p1
%patch1173 -p1
%patch1174 -p1
%patch1175 -p1
%patch1176 -p1
%patch1177 -p1
%patch1178 -p1
%patch1179 -p1
%patch1180 -p1
%patch1181 -p1
%patch1182 -p1
%patch1183 -p1
%patch1184 -p1
%patch1185 -p1
%patch1186 -p1
%patch1187 -p1
%patch1188 -p1
%patch1189 -p1
%patch1190 -p1
%patch1191 -p1
%patch1192 -p1
%patch1193 -p1
%patch1194 -p1
%patch1195 -p1
%patch1196 -p1
%patch1197 -p1
%patch1198 -p1
%patch1199 -p1
%patch1200 -p1
%patch1201 -p1
%patch1202 -p1
%patch1203 -p1
%patch1204 -p1
%patch1205 -p1
%patch1206 -p1
%patch1207 -p1
%patch1208 -p1
%patch1209 -p1
%patch1210 -p1
%patch1211 -p1
%patch1212 -p1
%patch1213 -p1
%patch1214 -p1
%patch1215 -p1
%patch1216 -p1
%patch1217 -p1
%patch1218 -p1
%patch1219 -p1
%patch1220 -p1
%patch1221 -p1
%patch1222 -p1
%patch1223 -p1
%patch1224 -p1
%patch1225 -p1
%patch1226 -p1
%patch1227 -p1
%patch1228 -p1
%patch1229 -p1
%patch1230 -p1
%patch1231 -p1
%patch1232 -p1
%patch1233 -p1
%patch1234 -p1
%patch1235 -p1
%patch1236 -p1
%patch1237 -p1
%patch1238 -p1
%patch1239 -p1
%patch1241 -p1
%patch1242 -p1
%patch1243 -p1
%patch1244 -p1
%patch1245 -p1
%patch1246 -p1
%patch1247 -p1
%patch1248 -p1
%patch1249 -p1
%patch1250 -p1
%patch1251 -p1
%patch1252 -p1
%patch1253 -p1
%patch1254 -p1
%patch1255 -p1
%patch1256 -p1
%patch1257 -p1
%patch1258 -p1
%patch1259 -p1
%patch1260 -p1
%patch1261 -p1
%patch1262 -p1
%patch1263 -p1
%patch1264 -p1
%patch1265 -p1
%patch1266 -p1
%patch1267 -p1
cp %{SOURCE1} .

%build
%define _sbindir /sbin
%define _libdir /%{_lib}
%define _libmpathdir %{_libdir}/multipath
make %{?_smp_mflags} LIB=%{_lib} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}

make install \
	DESTDIR=%{buildroot} \
	bindir=%{_sbindir} \
	syslibdir=%{_libdir} \
	libdir=%{_libmpathdir} \
	rcdir=%{_initrddir}

# tree fix up
# install -m 0644 %{SOURCE1} %{buildroot}/etc/multipath.conf
install -d %{buildroot}/etc/multipath

%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add multipathd
if [ "$1" -gt "1" -a ! -e /etc/multipath/bindings -a \
    -f /var/lib/multipath/bindings ]; then
	mv /var/lib/multipath/bindings /etc/multipath/bindings
	ln -s /etc/multipath/bindings /var/lib/multipath/bindings
fi

%preun
if [ "$1" = 0 ]; then
	/sbin/service multipathd stop /dev/null 2>&1
	/sbin/chkconfig --del multipathd
fi

%postun
if [ "$1" -ge "1" ]; then
	/sbin/service multipathd condrestart >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%{_sbindir}/multipath
%{_sbindir}/multipathd
%{_sbindir}/cciss_id
%{_sbindir}/mpathconf
%{_sbindir}/mpathpersist
%{_initrddir}/multipathd
%{_mandir}/man3/mpath_persistent_reserve_in.3.gz
%{_mandir}/man3/mpath_persistent_reserve_out.3.gz
%{_mandir}/man5/multipath.conf.5.gz
%{_mandir}/man8/multipath.8.gz
%{_mandir}/man8/multipathd.8.gz
%{_mandir}/man8/mpathconf.8.gz
%{_mandir}/man8/mpathpersist.8.gz
%config /lib/udev/rules.d/40-multipath.rules
%doc AUTHOR COPYING FAQ
%doc multipath.conf multipath.conf.annotated
%doc multipath.conf.defaults multipath.conf.synthetic
%dir /etc/multipath

%files libs
%defattr(-,root,root,-)
%doc AUTHOR COPYING
%{_libdir}/libmultipath.so
%{_libdir}/libmpathpersist.so
%{_libdir}/libmpathpersist.so.*
%dir %{_libmpathdir}
%{_libmpathdir}/*

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files -n kpartx
%defattr(-,root,root,-)
/sbin/kpartx
%{_mandir}/man8/kpartx.8.gz

%changelog
* Thu Jan  5 2017 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.100
- Modify 0261-RHBZ-1377532-disable-changed-paths.patch
  * add man page information
- Refresh 0265-RHBZ-1355669-max-sectors-kb.patch
- Related: #1377532

* Tue Dec  6 2016 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.99
- Change devicemapper Requires to >= 1.02.117-10.el6 (bz #1344381)
- Resolves: #1344381

* Tue Dec  6 2016 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.98
- Add 0266-RHBZ-1401391-fix-prio-put.patch
  * don't try to drop a nonexistant prio handler
- Add 0267-RHBZ-1401769-orphan-status.patch
  * don't print out checker and device status for orphan paths
- Resolves: bz #1401391, #1401769

* Thu Nov 10 2016 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.97
- Add 0265-RHBZ-1355669-max-sectors-kb.patch
  * add "max_sectors_kb" config option to set this value on all paths
- Change devicemapper Requires to >= 1.02.117-9.el6 (bz #1344381)
  * forces multipath to use latest version of blk-availability
- Resolves: bz #1344381, #1355669

* Thu Nov  3 2016 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.96
- Add 0258-UPBZ-1300414-PURE_config.patch
- Add 0264-RHBZ-1365710-no-use-after-free.patch
  * Fix two segfaults, and NULL out some structures after free
- Add 0265-RHBZ-1390472-dont-exit.patch
  * don't exit if multipath hits recoverable errors during startup
- Resolves: bz #1300414, #1365710, #1390472

* Fri Oct 14 2016 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.95
- Modify 0254-RHBZ-1310320-no-kpartx.patch
  * fix small bug with unitialized data
- Refresh 0261-RHBZ-1377532-disable-changed-paths.patch
- Add 0262-RH-free-vector.patch
  * Fix coverity discovered bug in error path
- Resolves: bz #1310320

* Fri Oct 14 2016 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.94
- Add 0251-RHBZ-1349376-fix-makefile.patch
  * make multipath use correct version of libdevmapper
- Add 0252-RHBZ-1333334-huawei-config.patch
- Add 0253-RHBZ-1305589-check-multipathd.patch
  * warn if multipath devices exist and mutipathd is not running
- Add 0254-RHBZ-1310320-no-kpartx.patch
  * add skip_kpartx option to skip kpartx device creation
- Add 0255-UPBZ-1322532-disable-reinstate.patch
  * do not reinstate unusable Implicit ALUA ghost paths
- Add 0256-RHBZ-1324764-man-page-typo.patch
- Add 0257-UPBZ-1328077-resize-map.patch
  * reset size if resizer operation fails
- Add 0259-UPBZ-1343747-dont-fail-discovery.patch
  * keep multipath from failing if it fails to get information on any device
- Add 0260-RHBZ-1364879-check-mpath-prefix.patch
  * ignore all devices that don't have a uuid starting with "mpath-"
- Add 0261-RHBZ-1377532-disable-changed-paths.patch
  * do not use path devices that change their wwid
- Resolves: bz #1299644, #1305589, #1310320, #1322532, #1324764, #1328077
- Resovles: bz #1333334, #1343747, #1349376, #1364879, #1377532

* Wed Mar  9 2016 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.93
- Add 0250-RHBZ-1316165-fix-i686-size-bug.patch
  * make multipathd use uint64_t for tracking the interactive command
    fingerprint.
- Resolves: bz #1316165

* Fri Feb 19 2016 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.92
- Modify 0246-RHBZ-1145442-raw-output-and-wildcards.patch
  * fix PAD and PRINT macros
- Resolves: bz #1145442

* Thu Feb 18 2016 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.91
- Add 0249-RHBZ-1208521-fix-typo-configure.patch
  * fix output typo
- Resolves: bz #1208521

* Thu Jan  7 2016 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.90
- Add 0248-RHBZ-1289353-alua-pref-arg.patch
  * add exclusive_pref_bit argument to the alua prioritizer
- Resolves: bz #1289353

* Mon Nov 23 2015 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.89
- Add 0247-RHBZ-1283181-fix-remove-crash.patch
  * Check is sysdev is NULL before dereferencing
- Resolves: bz #1283181

* Tue Nov 17 2015 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.88
- Add 0233-RHBZ-1215903-remove-pg-timeout.patch
- Add 0234-RHBZ-818404-update-doc.patch
- Add 0235-RHBZ-1033789-rdac-update.patch
  * Don't use trasntioning controllers
- Add 0236-RH-per-path-prio.patch
  * Paths now store their own prio structure, instead of pointing
    to a global one
- Add 0237-RHBZ-1081395-save-alua-info.patch
  * Save alua information in prioritizer to speed access
- Add 0238-RHBZ-1153704-async-timeout.patch
  * Make directio use the checker_timeout in async mode
- Add 0239-RHBZ-1201444-update-eternus-config.patch
- Add 0241-RHBZ-1214127-fix-help.patch
- Add 0242-RHBZ-1238507-kpartx-fix.patch
  * Don't overwrite already in use partitions
- Add 0243-RHBZ-1248177-reset-alias.patch
  * Use existing alias on failed rename
- Add 0244-RHBZ-1254692-kpartx-sync.patch
  * kpartx runs in sync mode by default
- Add 0245-RHBZ-1273829-autodetect-readonly-devs.patch
  * auto-reload devices as RO when a path turns RO
- Add 0246-RHBZ-1145442-raw-output-and-wildcards.patch
  * and raw output and more wildcards
- Modify device-mapper Requires
  * Require version with deferred remove support
- Resolves: bz #818404, #1033789, #1081395, #1145442, #1153704, #1187278
- Resolves: bz #1201444, #1208521, #1214127, #1215903, #1238507, #1248177
- Resolves: bz #1254692, #1273829


* Wed Mar 11 2015 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.87
- Modify 0228-RHBZ-1072081-delayed-reintegration.patch
  * print "no" instead of "off"
- Resolves: bz #1072081

* Tue Mar 10 2015 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.86
- Modify 0228-RHBZ-1072081-delayed-reintegration.patch
  * Change show config output
- Resolves: bz #1072081 

* Tue Mar  3 2015 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.85
- Modify 0228-RHBZ-1072081-delayed-reintegration.patch
  * Fix checker name printing issue
- Resolves: bz #1072081

* Thu Feb 19 2015 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.84
- Add 0228-RHBZ-1072081-delayed-reintegration.patch
  * Add "delay_watch_checks" and "delay_wait_checks" options to delay
    reintegration of flakey paths.
- Add 0229-UPBZ-1168987-queue_if_no_path_issue.patch
  * Make sure no_path_retry is properly set even if there are no active paths.
- Add 0230-RHBZ-880121-fix-double-free.patch
  * multipath was freeing the multipath alias twice if it failed to create the
    multipath device.
- Add 0231-RHBZ-978947-dell-36xxi.patch
  * new builtin configurations.
- Add 0232-RHBZ-997028-autodetect-clariion-alua.patch
  * configure multipath to automatically detect alua settings on clariion
    devices.
- Resolves: bz #880121, #978947, #997028, #1072081, #1168987

* Fri Jan 23 2015 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.83
- Add 0223-UPBZ-1120047-change-alua-prio.patch
  * Paths with the pref bit set will no longer be in pathgroups by
    themselves, if there are other paths that they could be load
    balanced with.
- Add 0224-UPBZ-1148096-reload-on-rename.patch
  * multipath will reload a table even if it also renames the device
- Add 0225-UPBZ-1148096-user-friendly-name-remap.patch
  * multipath will default to continue using the existing
    user_friendly_name
- Add 0226-RHBZ-1006895-add-config_dir-option.patch
  * multipath will now also read its configuration from files with
    the .conf suffix in the directory specified by config_dir
    which defaults to /etc/multipath/conf.d
- Add 0227-RHBZ-1171862-thread-safe.patch
  * only multipathd will keep a global cache of sysfs information
    for paths.
- Resolves: bz #1006895, #1120047, #1148096, #1171862

* Tue Jan  6 2015 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.82
- Add 0220-RHBZ-1128786-dont-show-pg-timeout.patch
  * remove pg_timeout from chow config
- Add 0221-RHBZ-1175888-add-wwid-option.patch
  * add multipath option "-a". To add a device's wwid to the wwids file
- Add 0222-RHBZ-1175888-cmdline-wwid.patch
  * make multipathd read wwids specified by the kernel commandline mpath.wwid
    option on startup.
- Resolves: bz #1128786, #1175888

* Tue Nov 10 2014 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.81
- Add 0219-RHBZ-1136966-fix-partition-mapping-creation-race-with-kpartx.patch
  * Only run kpartx on device activation
- Resolves: bz #1136966

* Tue Jul 29 2014 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.80
- Add 0218-RHBZ-1117714-configure-missing-devs.patch
  * handle externally removed devices during configuration.
- Resolves: bz #1117714

* Tue Jun 24 2014 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.79
- Modify 0198-RHBZ-1080052-orphan-paths-on-reload.patch
  * Fix case where pathlist wasn't getting updated properly
- Related: bz #1080052

* Tue Jun 17 2014 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.78
- Modify 0196-RHBZ-1012672-fix-sysdev.patch
  * remove unused function, and fix NULL ptr dereference
- Modify 0211-UPBZ-1088013-reorder-paths-for-round-robin.patch
  * Fix some pointer errors
- Modify 0213-RHBZ-1069641-config-error-checking.patch
  * Stop allocating extra memory in config parser.
- Related: bz #1049637, #1069641, #1088013

* Wed Jun  4 2014 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.77
- Add 0214-RHBZ-1078485-configurable-prio-timeout.patch
  * checker_timeout now adjusts the timeouts of the prioritizers as well.
- Add 0215-RHBZ-1054747-add-noasync-option.patch
  * Add a new defaults option, "force_sync", that disables the async mode
    of the path checkers. This is for cases where to many parallel checkers
    hog the CPU
- Add 0216-RHBZ-1095868-multipathd-man-typo.patch
- Add 0217-RHBZ-1101101-add-w-options.patch
  * multipath now includes the -w and -W options. -w makes multipath remove
    a wwid from the wwids file. -W removes all of the wwids, except for the
    ones belonging to the current multipath devices, from the bindings file.
- Resolves: bz #1078485, #1054747, #1095868, #1101101

* Thu May 22 2014 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.76
- Add 0207-UPBZ-1027061-sg-read-use-buffsize.patch
  * make readsector0 checker calculate the number of blocks to read based
    on the buffer size and the block size
- Add 0208-UPBZ-1028220-datacore-config.patch
  * Add support for DataCore Virtual Disk
- Add 0209-RHBZ-999766-update-annotated.patch
  * update multipath.conf.annotated
- Add 0210-UPBZ-1099932-fast-io-fail-iscsi.patch
  * and iscsi support for fast_io_fail_tmo
- Add 0211-UPBZ-1088013-reorder-paths-for-round-robin.patch
  * make multipathd order paths for better throughput in round-robin mode
- Add 0212-RHBZ-1086417-orphan-path-on_failed-add.patch
  * If multipathd fails to add path correctly, it now fully orphans the path
- Add 0213-RHBZ-1069641-config-error-checking.patch
  * Improve multipath.conf error checking.
- Resolves: bz #1027061, #1028220, #999766, #1099932, #1088013, #1086417
- Resolves: bz #1069641

* Wed Apr 23 2014 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.75
- Add 0196-RHBZ-1012672-fix-sysdev.patch
  * rewrite multipath sysfs device handling to fix various issues from
    bzs #1012672, #1064636, and #1049637
- Add 0197-RHBZ-1049315-netapp-rw-change.patch
  * allow reload_readwrite to be set by device, and set it by default for
    netapp devices.
- Add 0198-RHBZ-1080052-orphan-paths-on-reload.patch
  * make multipath orphan paths that are no longer included in the device
    when the table is reread.
- Add 0199-RHBZ-1007719-multipath-man.patch
  * documentation update
- Add 0200-RHBZ-1009061-allow_devt.patch
  * allow specifying paths to multipath by major:minor, instead of devname
- Add 0201-RHBZ-1018697-cli-use-basename.patch
  * make multipathd interactive commands accept device names that start with
    /dev/
- Add 0202-RHBZ-1024604-weighted-prio-man.patch
  * documentation update
- Add 0203-RHBZ-1054046-mpathconf-typo.patch
  * fix command output typo
- Add 0204-RHBZ-1067102-doc-add-selectors.patch
  * documentation update
- Add 0205-RHBZ-1072974-alua-typo.patch
  * fix priritizer output typo
- Add 0206-UPBZ-1020556-e-series-config.patch
  * udpate E-Series config to autodetect prio and hardware handler.
- Resolves: bz #1049637, #1064636, #1049315, #1080052, #1007719, #1009061
- Resolves: bz #1018697, #1024604, #1054046, #1067102, #1072974, #1020556

* Wed Mar 19 2014 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.74
- Add 0195-UPBZ-1024103-alua-prio-timeout.patch
  * change alua prioritizer timeout from 5 minutes to one minute
- Resolves: bz #1024103

* Mon Feb 24 2014 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.73
- Add 0194-RHBZ-997570-no-sync-turs-on-pthread_cancel.patch
  * If async tur checker fails on threads, don't retry with the sync version
- Resolves: bz #997570

* Fri Oct 11 2013 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.72
- Add 0193-UPBZ-1011341-dos-4k-partition-fix.patch
  * Make kpartx correctly handle 4K sector size devices with dos partitions.
- Resolves: bz #1011341

* Wed Sep 25 2013 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.71
- Add 0192-RHBZ-916667-print-major-minor.patch
  * Make multipathd print major:minor on path and and remove events
- Resolves: bz #916667

* Mon Aug 19 2013 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.70
- Modify 0185-RH-signal-waiter.patch
  * making the waiter threads exit correctly caused a race at shutdown.
- Resolves: bz #996921

* Mon Aug 12 2013 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.69
- Add 0188-RH-add-all_devs.patch
  * Add new special "all_devs" devices identifier, that makes multipath
    update a the values on all devices
- Add 0189-RHBZ-986767-blacklist-td-devs.patch
  * add td[a-z].* devices to the builtin blacklist
- Add 0190-UPBZ-994277-handle-offline-states.patch
  * Handle "transport-offline" and "quiesce" path states
- Add 0191-UPBZ-995251-fail-rdac-on-unavailable.patch
  * make rdac checker always mark paths with asymmetric access state of
    unavailable as down
- Resolves: bz #986767, #994277, #995251

* Mon Jul  8 2013 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.68
- Modify 0172-RHBZ-895110-fix-output-buffer.patch
  * free buffer
- Modify 0182-RHBZ-947798-rw-change.patch
  * don't access multipath device if it has been freed in setup_multipath
- Add 0187-RH-fix-bad-derefs.patch
  * Fix places where we are dereferencing freed pointers
- Resolves: bz #947798

* Tue Jul  2 2013 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.67
- Modify 0182-RHBZ-947798-rw-change.patch
  * Add documentation
- Modify 0183-RHBZ-924924-replace_whitespace.patch
  * Add documentation
- Add 0186-RHBZ-974129-delay_set_fast_io_fail.patch
  * fix issue with setting fast_io_fail_tmo past the old value of
    dev_loss_tmo
- Resolves: bz #974129, #924924, #947798

* Mon Jun 24 2013 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.66
- Modify 0179-RHBZ-920448-bindings-fix.patch
  * remove debug printing.
- Add 0181-RHBZ-958091-check-for-erofs.patch
  * only retry loading a map read-only if the read/write load failed
    with EROFS
- Add 0182-RHBZ-947798-rw-change.patch
  * add a new multipath.conf default keyword "reload_readwrite". If set
    to "yes", multipathd will listed to path device change events, and
    if they device has become read/write, it will reload the multipath
    device.
- Add 0183-RHBZ-924924-replace_whitespace.patch
  * add a new multipath.conf default keyword "replace_wwid_whitespace".
    If set to "yes", multipath will add --replace-whitespace for devices
    That use the default getuid callout.
- Add 0184-RHBZ-975676-fix_cli_resize.patch
  * deal with resize happening while path device is being removed.
- Add 0185-RH-signal-waiter.patch
  * send waiter thread a signal to break out of waiting for dm events
- Resolves: bz #958091, #947798, #924924, #975676

* Tue Jun 10 2013 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.65
- Add 0168-RHBZ-902585-fix-state-size.patch
- Add 0169-RHBZ-895110-fix-params-size.patch
- Add 0170-RHBZ-889441-fix-multipath.rules.patch
  * set multipath device link_priority on change events
- Add 0171-RHBZ-904836-handle-other-sector-sizes.patch
  * handle non-512 byte GPT sector sizes
- Add 0172-RHBZ-895110-fix-output-buffer.patch
  * make sure to allocate enough space to print the full list of multipath
    devices
- Add 0173-RHBZ-889429-catch-early-uevents.patch
  * start up the uevent listening thread early, but don't start up the
    uevent servicing thread until after you configure
- Add 0174-RHBZ-875199-null-vector-fix.patch
- Add 0175-RHBZ-889987-detect_prio_fix.patch
  * make sure you can actually get the priority with ALUA before selecting it.
- Add 0176-RHBZ-892292-listing-speedup.patch
  * don't get the wwid when you are just listing a device.
- Add 0177-RHBZ-902593-multipath-c-manpage.patch
- Add 0178-RHBZ-918825-kpartx-loop-devices.patch
  * remove tmp loopdev create by 'kpartx -l' in no partitions were found.
- Add 0179-RHBZ-920448-bindings-fix.patch
  * try to find the smallest unused user friendly name
- Add 0180-RHBZ-928831-check-dm-version-for-retain_hwhandler.patch
  * don't use retain_attached_hw_handler on kernels that don't support it.
- Resolves: bz #875199, #889429, #889441, #889987, #892292, #902585
- Resolves: bz #902593, #904836, #918825, #920448, #928831

* Tue Jan 22 2013 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.64
- Add 0167-RHBZ-735459-fix-mpathpersist-fns.patch
  * make reservation_key display correctly in "multipathd show config"
- Resolves: bz #735459

* Tue Dec  4 2012 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.63
- Add 0166-RHBZ-880487-make-path-fd-readonly.patch
  * revert change from 0152-RHBZ-735459-mpath_persist.patch, so that
    path fds are again opened O_RDONLY
- Resolves: bz #880487

* Thu Oct 25 2012 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.62
- Add 0165-RHBZ-869253-disable-libdm-failback.patch
  * multipathd and kpartx now set a flag to request device-mapper
    not create devices itself.
- Resolves: bz #869253

* Sat Oct 13 2012 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.61
- Modify 0156-RHBZ-813963-new-alua-prio.patch
  * fix minor porting issue
- Resolves: bz #813963

* Sat Oct 13 2012 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.60
- Add 0161-RHBZ-836890-AIX-whitespace.patch
- Add 0162-RHBZ-860748-early-blacklist.patch
  * blacklist devices as soon as possible
- Add 0163-RHBZ-839386-detect-prio.patch
  * add default and device configuration option detect-prio
- Add 0164-RHBZ-839386-netapp-config.patch
- Modify 0153-RHBZ-839386-retain_hwhandler.patch
  * cleanup minor issues
- Resolves: bz #836890, #860748, #839386

* Tue Oct  9 2012 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.59
- Add 0146-RHBZ-595692-fix-cciss-names.patch
  * convert cmdline cciss names to sysfs format
- Add 0147-RHBZ-824243-826610-833124-doc-fix.patch
- Add 0148-RHBZ-619173-storagetek-config.patch
- Add 0149-RHBZ-810788-remove-dups.patch
  * remove duplicates from builtin configs
- Add 0150-RHBZ-810755-update-conf-defaults.patch
- Add 0151-RHBZ-822389-fix-rename.patch
  * make multipath switch names on reload after disabling
    user_friendly_names
- Add 0152-RHBZ-735459-mpath_persist.patch
  * mpathpersist allows persistent reservatoins through multipath devices
- Add 0153-RHBZ-839386-retain_hwhandler.patch
  * add retain_attached_hw_handler default and multipaths config option
- Add 0154-RHBZ-578114-kpartx-retry.patch
  * retry on EBUSY for loop device deletes
- Add 0155-RHBZ-810989-load-modules.patch
  * service multipathd start loads kernel modules
- Add 0156-RHBZ-813963-new-alua-prio.patch
  * combine the "alua" and "tpg_pref" prioritizers
- Add 0157-RHBZ-816717-flush-full-paths.patch
  * make multipath accept full pathnames in -f
- Add 0158-RHBZ-821885-check-blacklist.patch
  * make multipath -c check the device blacklisting
- Add 0159-RHBZ-818367-829065-rdac.patch
- Add 0160-RHBZ-841732-dont-swap-devices.patch
- Resolves: bz #595692, #824243, #826610, #833124, #619173, #810788, #810755
- Resolves: bz #822389, #735459, #839386, #578114, #810989, #813963, #816717
- Resolves: bz #821885, #818367, #829065, #841732

* Mon Aug 27 2012 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.58
- Modify multipath.conf
  * change "selector" to "path_selector"
- Resolves: bz #827072

* Tue Jul  3 2012 Benjmain Marzinski <bmarzins@redhat.com> -0.4.9.57
- Add 0145-RHBZ-831045-realloc-vector.patch
  * fix deleting items from vector, and handle error cases
- Resolves: bz #831045

* Thu Apr 26 2012 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.56
- Modify 0137-RHBZ-799842-change-netapp-config.patch
  * Add pg_init_retries to netapp config
- Add 0144-RHBZ-812832-shutdown-crash.patch
  * kill waiter threads with pthread_cancel() instead of SIGUSR1
- Resolves: bz #799842, #812832

* Wed Apr 25 2012 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.55
- Modify 0131-RHBZ-662433-override-queue-no-daemon.patch
  * enforce queueing on condrestart as well
- Add 0142-RHBZ-769527-fix-features-build.patch
  * remove "queue_if_no_path" feature when flushing due to
    "flush_on_last_del"
- Add 0143-RHBZ-467709-followover-chkr-state.patch
  * Only failback if the path checker's reported state has changed
- Resolves: bz #467709, #769527
- Related: bz #662433

* Tue Apr 10 2012 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.54
- Modify 0132-RHBZ-744756-regex-hw-match.patch (bz #802630)
  * Added documentation to the multipath.conf man page
- Modify 0138-RH-fix-strings.patch (bz #810208)
- Resolves: bz #802630, #810208

* Thu Mar 29 2012 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.53
- Add 0141-RHBZ-752989-remove-dup-configs.patch
- Related: bz #752989

* Thu Mar 29 2012 Benjamin Marzinski <bmarzins@redaht.com> -0.4.9.52
- Modify 0130-RHBZ-754586-use-sync-support.patch
  * This fix now just calls dm_task_update_nodes() after renaming the
    the devices.
- Refresh 0110-RHBZ-725541-04-serialize-startup.patch
- Refresh 0131-RHBZ-662433-override-queue-no-daemon.patch
- Refresh 0135-RHBZ-798541-build-options.patch
- Resolves: bz #805809

* Thu Mar 22 2012 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.51
- Add 0139-RHBZ-800288-netapp-devloss.patch
  * Set fast_io_fail_tmo and dev_loss_tmo for netapp devices
- Add 0140-RHBZ-803527-blacklist-management-luns.patch
- Resolves: bz #800288, #803527

* Thu Mar 15 2012 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.50
- Modify 0135-RHBZ-798541-build-options.patch
  * switch from compiling with -lpthread to -pthread, to make sure
    and use reentrant versions of functions.
- Related: bz #798541

* Tue Mar 13 2012 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.49
- Modify 0132-RHBZ-744756-regex-hw-match.patch
  * The regex comparison was working in the wrong direction.
- Modify 0133-RHBZ-744210-config-changes.patch
  * add missing entries to store_hwe
- Add 0135-RHBZ-798541-build-options.patch
  * build rpm with RPM_OPT_FLAGS
- Add 0136-RHBZ-799908-ibm-xiv.patch
- Add 0137-RHBZ-799842-change-netapp-config.patch
- Add 0138-RH-fix-strings.patch
  * fix two spots where multipath wasn't checking string size before copying
- Pass RPM_OPT_FLAGS to make
- Resolves: bz #798541, #799842, #799908
- Related: bz #744210, #744756

* Sun Mar  4 2012 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.48
- Add 0124-RHBZ-751039-fix-shutdown.patch
  * make sure to test if the threads have been cancelled after locking
- Add 0125-RHBZ-727429-dont-print-exec-fails.patch
- Add 0126-RHBZ-740760-kpartx-man-page.patch
- Add 0127-RHBZ-737051-add-netapp-brand.patch
- Add 0128-RHBZ-796384-fix-alua.patch
  * gerneralize the vpd 0x83 handling
- Add 0129-RHBZ-788963-eternus-config.patch
- Add 0130-RHBZ-754586-use-sync-support.patch 
  * multipathd and kpartx now use udev_sync_support. They just don't
    use any cookies
- Add 0131-RHBZ-662433-override-queue-no-daemon.patch
  * make queue_without_daemon default to off, but make service restart
    override that so, you won't fail IO on restart.
- Add 0132-RHBZ-744756-regex-hw-match.patch
  * add hwtable_regex_match parameter, which makes the user device entries
    in multipath.conf regex with the builtin ones to override them.
- Add 0133-RHBZ-744210-config-changes.patch
  * default max_fs to "max" and make user_friendly_names configurable in
    the devices and multipaths section.
- Add 0134-RHBZ-769527-fix-flush-on-last-del.patch
- Resolves: bz #662433, #727429, #737051, #740760, #744210, #744756, #751039
- Resolves: bz #754586, #769527, #788963, #796384

* Mon Jan 30 2012 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.47
- Readd 0107-RHBZ-725541-01-async-tur-checker.patch
- Add 0119-RHBZ-747604-fix-async-tur.patch (BZ #760852)
  * keep a reference count on the checker context to keep from freeing it
    while its still in use.
- Add 0120-RHBZ-752989-tighten_vendor_product_regex.patch
  * Some of the vendor and product regexes were matching incorrect devices
    because they were too broad.
- Add 0121-RHBZ-751938-fix-usage-return.patch
  * Make -h return 0
- Add 0122-RHBZ-750132-fix-oom-adj.patch
  * use oom_score_adj instead of oom_adj
- Add 0123-RHBZ-732932-fix-coverity-issues.patch
  * don't leak reply if update_multipath fails.
- Update multipath.conf (BZ #702222)
  * Add a comment reminding users to reload multipathd after editting
    their config
- Resolves: bz #702222, #732932, #750132, #751938, #752989, #760852

* Wed Oct  5 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.46
- Remove 0107-RHBZ-725541-01-async-tur-checker.patch
  * This patch caused a regression where, multpathd could corrupt is memory
    when a path was deleted (bz747604)
- Refresh 0110-RHBZ-725541-04-serialize-startup.patch
-Resolves: bz #747604


* Wed Oct  5 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.45
- Add 0118-RHBZ-738298-revert-631009.patch
  * reverts most of 0101-RHBZ-631009-disable-udev-disk-rules-on-reload.patch
    but still allows the -u option, for compatibility
- Resolves: bz #738298

* Thu Sep 22 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.44
- Add 0116-RH-manpage-update.patch
  * update the manpages with new features
- Add 0117-RHBZ-697386-logger-shutdown-crash.patch
  * The main multipathd thread was racing with the logger, now it
    waits for the logger thread to shutdown first.
- Resolves: bz #697386

* Sun Aug 14 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.43
- Add 0102-RHBZ-714821-dont-remove-map-twice.patch
  * multipathd was removing a map twice in one code path, causing
    double free errors
- Add 0103-RHBZ-725541-09-no-partitions.patch
  * if a device has the "no_partitions" feature, kpartx ignores it
- Add 0104-RHBZ-725541-10-force-devmap.patch
  * override "no_partitions"
- Add 0105-RHBZ-725541-08-reset-running.patch
  * abort timed-out IO in directio checker
- Add 0106-RHBZ-725541-07-tur-checker-reservation-conflict.patch
  * don't count a path as down if it has a reservation conflict. The
    kernel should be failing these errors up past multipath now.
- Add 0107-RHBZ-725541-01-async-tur-checker.patch
  * Make tur checker async
- Add 0108-RHBZ-725541-06-offline-check.patch
  * Don't get the priority of offline devies.
- Add 0109-RHBZ-725541-05-only-count-up-and-ghost-paths.patch
  * fix path counting
- Add 0110-RHBZ-725541-04-serialize-startup.patch
  * add the "show daemon" multipathd command, so users can check
    that the daemon has started up completely.
- Add 0111-RHBZ-725541-03-handle-LBA_DEPENDENT-state.patch
  * handle LBA_DEPENDENT alua state.
- Add 0112-RHBZ-725541-02-infinite-dev-loss-tmo.patch
  * allow dev_loss_tmo to be set to "inifinty", which sets it to
    the maximum allowed value.
- Add 0113-RHBZ-719571-validate-guid-partitions.patch
  * don't build partition devices for invalid gpt's.
- Add 0114-RHBZ-723168-adjust-messages.patch
- Add 0115-RHBZ-713754-lower-minio.patch
  * add rr_min_io_rq parmeter, that sets the min_io to 1 for
    request based multipath
Resolves: bz #699577, #713754, #714821, #719571, #723168, #725541

* Wed Jun 29 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.42
- Add 0089-RHBZ-694602-RSSM-config.patch
- Add 0090-RHBZ-700169-fix-nr-active.patch
  * Make sure to always count ghost paths as active
- Add 0091-RHBZ-699577-manpage-clarification.patch
- Add 0092-RHBZ-689504-rdac-retry.patch
  * Make the rdac checker retry up to 5 times on errors that are likely
    transient.
- Add 0093-RHBZ-677449-dont-remove-map-on-enomem.patch
  * Don't remove a multipath device if dm_map_present fails due to lack of
    memory
- Add 0094-RHBZ-707560-check-return-value.patch
  * Don't try to update path groups on a path priority change if the 
    multipath device has disappeared.
- Add 0095-RHBZ-678673-no-path-groups.patch
  * Allow multipath devices with no path groups
- Add 0096-RHBZ-683616-ioship-support.patch
  * Modify the rdac checker to work better storage in IOSHIP mode
- Add 0097-RHBZ-697386-fix-shutdown-crash.patch
  * Add missing test for thread cancellation to the checker thread.
- Add 0098-RHBZ-706555-dont-update-pgs-in-manual.patch
  * When failback is set to manual, do not automatically reconfigure the
    pgs when a path changes priority
- Add 0099-RHBZ-705854-warn-on-bad-dev-loss-tmo.patch
- Add 0100-RHBZ-710478-deprecate-uid-gid-mode.patch
  * uid, gid and mode are now controlled by udev.
- Add 0101-RHBZ-631009-disable-udev-disk-rules-on-reload.patch
- Remove 0082-RHBZ-631009-disable-udev-disk-rules-on-reload.patch
  * multipath and kpartx now have a "-u" option that forces the udev
    dm-disk rules to run.
- Resolves: bz #694602, #700169, #689504, #677449, #707560, #678673
- Resolves: bz #683616, #697386, #706555, #705854, #710478, #631009
  

* Mon Apr 19 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.41
- Add 0088-RHBZ-693524-fix-prio-segfault.patch
   * Don't reuse the the path argument as a variable in the vector
     loop.
- Resolves: bz# 696157

* Mon Mar 14 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.40
- Add 0087-RHBZ-680480-skip-if-no-sysdev.patch
   * Don't check the path if it has no sysdev, since it is about to
     be removed.
- Resoves: bz# 680480

* Mon Mar  9 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.39
- Add 0086-RHBZ-681144-sysfs-device-cleanup.patch
   * Make sure to remove the sysfs device from cache when the path is
     removed. Also, only search the sysfs device cache under the vecs lock
- Resolves: bz #681144

* Mon Feb 21 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.38
- Remove 0082-RHBZ-631009-disable-udev-disk-rules-on-reload.patch
   * This patch was causing a serious regression (677937), and resolving
     it requires changes in /etc/rc.sysinit, so I'm backing it out for
     now.
- Resolves: bz #677937
- Related: bz #631009

* Mon Feb  3 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.37
- Add 0085-RHBZ-645605-fix-offline-check.patch
   * Make path_offline return false if it can't deterime a paths state.
- Rename 0080-RHBZ-622731-fix-no-config-value-segfault.patch to
         0080-RHBZ-662731-fix-no-config-value-segfault.patch
   * accidentally used the wrong bug number
- Resolves: bz #645605, #662731

* Mon Jan 31 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.36
- Add 0084-RHBZ-644111-read-only-bindings.patch
    * Add -B multipath and multipathd option, to make the bindings file
      read-only. This is to be used by the initramfs
- Resolves: bz #644111

* Sun Jan 23 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.35
- Add 0082-RHBZ-631009-disable-udev-disk-rules-on-reload.patch
    * Set DM_UDEV_DISABLE_DISK_RULES_FLAG in dm_simplecmd to stop blkid from
      running on reloads
- Add 0083-RHBZ-636213-633643-new-configs.patch
    * Autoconfigs for HP P2000 family and NEC Storage M Series arrays
- Resolves: bz #631009, #636213, #636213

* Mon Jan 10 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.34
- Add 0081-RHBZ-623644-fix-sysfs-caching.patch
    * Remove attribute value caching, and free cached parent devices on remove
- Resolves: bz #623644

* Mon Dec 20 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.33
- Add 0073-RHBZ-650664-clarify-error-msg.patch
    * tell users to increase max_fds, if multipath gets EMFILE trying to
      open a file.
- Add 0074-RHBZ-602883-dont-print-change.patch
    * don't print messages for every change uevent
- Add 0075-RHBZ-576919-log-checker-err.patch
    * add log_checker_err default config option, to control the verbosity
      of repeated checker error messages
- Add 0076-RHBZ-599690-update-multipath-conf.patch
- Add 0077-RHBZ-622608-nvdisk-config.patch
- Add 0078-RHBZ-628095-config-warnings.patch
    * print warning messages for invalid config parameters
- Add 0079-RHBZ-650797-display-iscsi-tgt-name.patch
    * get tgt name for iscsi devices
- Add 0080-RHBZ-622731-fix-no-config-value-segfault.patch
    * check that a config option has a value before trying to get the
      strlen of the value.
- Resolves: bz #576919, #599690, #602883, #622608, #622731, #628095, #650664
- Resolves: bz #650797

* Sun Nov 21 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.32
- Add 0064-RHBZ-612173-fix-reverse-lookup.patch
    * don't terminate WWID at whitespace on reverse lookup.
- Add 0065-RHBZ-635088-update-priority.patch
    * refresh all priorities when a new path comes online
- Add 0066-RHBZ-636071-mpathconf-variable_names.patch
    * don't use DISPLAY variable name. It configs with X. Also, unset all
      the variable names, so this doesn't happen again.
- Add 0067-RHBZ-622569-symmetrix-config.patch
- Add 0068-RHBZ-632734-nvdisk-config.patch
- Add 0069-RHBZ-636246-hp-open-config.patch
- Add 0070-RHBZ-639037-hitachi-open-config.patch
- Add 0071-RHBZ-611779-fix-whitespace-crash.patch
    * get_cmdvec wasn't setting the passed in vector to NULL, when
      there was no command.
- Add 0072-RHBZ-651389-change-scsi-tmo-order.patch
    * Make multipath set fast_io_fail_tmo before dev_loss_tmo, so that
      you can set dev_loss_tmo above 600.
- Resolves: bz #651389, #611779, #639037, #636246, #632734, #622569, #636071
- Resolves: bz #635088, #612173


* Tue Sep  7 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.31
- Modify 0063-RHBZ-595719-udev_link_priority.patch
    * make link_priority only work on multipath devices and partitions.
- Resolves: bz #595719

* Thu Sep  2 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.30
- Modify 0063-RHBZ-595719-udev_link_priority.patch
    * move link_priority line up in the udev rules. Hopefully this is the
      actual fix.
- Resolves: bz #595719

* Thu Sep  2 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.29
- Modify 0063-RHBZ-595719-udev_link_priority.patch
    * Change link priority from 5 to 10
- Resolves: bz #595719

* Wed Aug 18 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.28
- Add 0064-RHBZ-612173-fix-reverse-lookup.patch
   * Fix multipath's wwid bindings file reverse lookup
- Resolves: bz #612173

* Tue Aug 17 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.27
- Add 0063-RHBZ-595719-udev_link_priority.patch
   * Increase the priority of multipath symlinks
- Resolves: bz #595719

* Tue Aug 17 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.26
- Add 0062-RHBZ-592998-hpsc-config.patch
- Resolves: bz #592998

* Tue Aug  3 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.25
- Add 0061-RHBZ-620479-find-rport.patch
  * multipath now will correctly set the dev_loss_tmo and fast_io_fail_tmo
    for setups where a devices rport id doesn't match its target id.
- Resolves: bz #620479

* Tue Jul 20 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.24
- Modify 0055-RHBZ-602257-update-on-show-topology.patch
  * fix patch so that multipath only syncs with the kernel, and doesn't
    update other features
- Add 0060-RHBZ-606420-fix-remove-map.patch
  * multipathd will now only report a success for remove map when it
    actually succeeds.
- Resolves: bz #602257, #606420

* Mon Jun 28 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.23
- Add 0055-RHBZ-602257-update-on-show-topology.patch
  * make multipathd updated state with the kernel before showing topology
- Add 0056-RHBZ-603812-better-type-check.patch
  * only count files a path devices, if they are block devices, and are not
    device-mapper devices.
- Add 0057-RHBZ-607869-fix-resize.patch
  * use the resize calls that don't set noflush, when you reload for size
    changes.
- Add 0058-RHBZ-601665-assemble-features.patch
  * When multipathd reloads paths, add queue_if_no_path to the features
    based on the no_path_retry value.
- Add 0059-RHBZ-607874-handle-offlined-paths.patch
  * get the sysfs pathinfo in multipath if necessary, and only retry
    failed ev_add_path reloads 3 times.
- Resolves: bz #602257, #603812, #607869, #601665, #607874

* Fri Jun 18 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.22
- Modify 0034-RHBZ-579575-add-q-multipath-option.patch
  * close a pidfile file descriptor
- Add 0051-RHBZ-596156-mpathconf-man-page.patch
  * add the mpathconf man page
- Add 0052-RHBZ-601247-fix-path-adoption.patch
  * only verify existing paths during adoption when specified
- Add 0053-RHBZ-596323-remember_more_wwids.patch
  * make sure that all wwids are in /etc/multipath/wwids when you run
    multipath
- 0054-RHBZ-596319-rules-cleanup.patch
- Resolves: bz #596156, #601247, #596323
- Related: bz #579575

* Fri May 21 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.21
- Add 0044-RHBZ-591940-dont-clear-daemon.patch
  * multipathd was clearing the daemon config setting on reconfigure
- Add 0045-RHBZ-593379-dont-add-unknown-paths.patch
  * multipathd no longer pulls paths from map loads
- Add 0046-RHBZ-593426-move-adopt-path.patch
  * The patch 0037-RH-adopt-paths.patch was causing problems, so I moved
    the adopt paths call to where it would effect fewer codepaths.
- Add 0047-RHBZ-591608-only-switch-pgs-once.patch
  * multipathd was telling the kernel to switch pathgroups twice when
    restoring a path.
- Add 0048-RHBZ-592494-fix-user-configs.patch
  * User hardware configs were getting matched after default configs. Also
    configs were getting merged that weren't complete matches.
- Add 0049-RHBZ-591644-enhance-mpathconf.patch
  * multipath now loads the config before checking if the kenel_module is
    installed, and mpathconf now can load the module and chkconfig multipathd
- Add 0050-RHBZ-595400-fix-checker-tmo.patch
  * Multipath wasn't opening the right sysfs file to set the checker timeout.
Resolves: bz #591940, #593379, #593426, #592494, #591644, #595400

* Wed May 11 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.20
- Add 0038-RHBZ-587201-IBM-SGI.patch
- Add 0039-RHBZ-589153-manpage-update.patch
- Add 0040-RHBZ-587695-add-checker-msg-alias.patch
  * The checker now prints the mutipathd device name with its message.
- Add 0041-RHBZ-587695-add-rdac-message.patch
  * The rdac checker now always prints a message, and the code is cleaner.
- Add 0042-RHBZ-590038-fix-fast-io-fail-tmo.patch
  * mutipath was trying using the wrong name to set fast_io_fail_tmo
- Add 0043-RHBZ-590028-close-sysfs_attr_fd.patch
  * mutipathd wasn't closing the fds for sysfs attribute files that it wrote
    to.
Resolves: bz #587201, #587695, #589153, #590028, #590038

* Wed May  5 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.19
- Add 0035-RHBZ-467709-add-followover.patch
  * Multipath now supports the failback option "followover". With this
    multipathd only fails back when a pathgroup first comes back online.
- Add 0036-RH-clear-messages.patch
  * keeps the checker from printing an old message if a new one isn't set.
- Add 0037-RH-adopt-paths.patch
  * Makes multipathd adopt paths when it updates the map.
- Resolves: bz #467709

* Thu Apr 15 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.18
- Refresh 0030-RHBZ-558636-check-if-multipath-owns-path.patch
- Modify 0021-RHBZ-558636-add-find-multipaths.patch
  * /etc/multipath/wwids now places the wwids inside of slashes to make
    sure that all valid wwids are supported.
- Add 0031-RHBZ-570546-display-avg-pg-prio.patch
- Add 0032-RHBZ-575767-ontap_prio.patc
  * change prio_netapp to prio_ontap
- Add 0033-RHBZ-573715-eurologic-config.patch
- Add 0034-RHBZ-579575-add-q-multipath-option.patch
  * multipath now will not set queue_if_no_path on a created or reloaded
    device unless multipathd is running.  This can be overridden by the -q
    option
- Resolves: bz #570546, #575767, #573715, #579575

* Mon Mar 22 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9.17
- Replace 0021-RHBZ-548874-add-find-multipaths.patch with
  0021-RHBZ-558636-add-find-multipaths.patch
  * Wrong bugzilla id.
- Modify 0012-RH-udev-sync-support.patch
- Modify 0022-RHBZ-557845-RHEL5-style-partitions.patch
  * patch 0012 didn't compiled without 0022 also applied. It now works correctly
    by itself.
- Add 0027-RHBZ-509443-enhance-show-config.patch
  * "multipathd show config" now show all default vaules, and all defined
    device and multipath values.
- Add 0028-RHBZ-452617-add-revision-parameter.patch
  * Adds a "revision" parameter to the devices section of multipath.conf,
    so configurations can be set by revision.
- Add 0029-RHBZ-567219-recalculate-pgs-in-checkerloop.patch
  * When the priority changes for a device that has groups it's pathgroups
    by priority, the pathgroups are recalculated.
- Add 0030-RHBZ-558636-check-if-multipath-owns-path.patch
  * multipath -c <devname> will check if a device has previously been assembled
    as a multipath path.  the multipath udev rules now set
    ENV{DM_MULTIPATH_DEVICE_PATH} if it has been.
- Resolves: bz #509443, #452617, #567219, #558636 

* Fri Mar 12 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-16
- Add 0025-RHBZ-508827-update-multipathd-manpage.patch
- Add 0026-RHBZ-549636-default-path-selector.patch
  * The default path selector paramter for multipath.conf is now named
    "path_selector" like it is for the device and multipath sections.
- Resolves: bz #508827, #549636

* Fri Feb 19 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-15
- Replace 0012-RH-explicitly-disable-dm-udev-sync-support-in-kpartx.patch with
  0012-RH-udev-sync-support.patch
  * Make kpartx and multipathd work with the udev sync cookies.
- Refresh 0013-RH-add-weighted_prio-prioritizer.patch
- Modify 0021-RHBZ-548874-add-find-multipaths.patch
  * fix a bug where mpathconf couldn't create a new multipath.conf file if one didn't
    already exist.
- Modify 0022-RHBZ-557845-RHEL5-style-partitions.patch
  * kpartx now creates 2 sector large devices for dos extended partitions, just
    like the partitions the kernel creates.
- Add 0023-RHBZ-557810-emc-invista-config.patch
- Add 0024-RHBZ-565933-checker-timeout.patch
  * All the checker functions that have explicit timeouts will now use
    /sys/block/sd<x>/device/timeout unless checker_timeout is set in multipath.conf
    If so, they will use that value instead.
- Resolves: bz #557810, #565933
- Related: bz #558636

* Fri Jan 22 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-14
- Add 0022-RHBZ-557845-RHEL5-style-partitions.patch
  * Make kpartx deal with logical partitions like it did in RHEL5.
    Don't create a dm-device for the extended partition itself.
    Create the logical partitions on top of the dm-device for the whole disk.
- Modify 0010-RH-multipath-rules-udev-changes.patch
  * Fix udev rules to use DM_SBIN_PATH when calling kpartx
  * install udev rules to /lib/udev/rules.d instead of /etc/udev/rules.d
- Refresh 0021-RHBZ-548874-add-find-multipaths.patch
- Resolves: bz #557845
* Fri Jan 15 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-13
- Refresh 0001-RH-queue-without-daemon.patch
- Refresh 0002-RH-path-checker.patch
- Modify 0010-RH-multipath-rules-udev-changes.patch
  * Modify udev rules as per Peter Jones' request.
- Modify 0014-RH-add-hp_tur-checker.patch
- Add 0003-for-upstream-default-configs.patch
- Add 0016-RHBZ-554561-fix-init-error-msg.patch
- Add 0017-RHBZ-554592-man-page-note.patch
- Add 0018-RHBZ-554596-SUN-6540-config.patch
- Add 0019-RHBZ-554598-fix-multipath-locking.patch
- Add 0020-RHBZ-554605-fix-manual-failover.patch
- Add 0021-RHBZ-548874-add-find-multipaths.patch
  * Added find_multipaths multipath.conf option
  * Added /sbin/mpathconf for simple editting of multipath.conf
- Resolves: bz #548874, #554561, #554592, #554596, #554598, #554605

* Tue Dec 15 2009 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-12
- Remove requirement on device-mapper with udev sync support, since
  the multipath udev rules can still work without it.
- Resolves: bz #548106

* Mon Nov 16 2009 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-11
- Add 0002-for-upstream-add-tmo-config-options.patch
  * Add fail_io_fail_tmo and dev_loss_tmo multipath.conf options
- Add 0013-RH-add-weighted_prio-prioritizer.patch
- Add 0014-RH-add-hp_tur-checker.patch
- Add 0015-RH-add-multipathd-count-paths-cmd.patch
- rename multipath.conf.redhat to multipath.conf, and remove the default
  blacklist.

* Tue Oct 27 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4.9-10
- Updated to latest upstream 0.4.9 code : multipath-tools-091027.tar.gz
  (git commit id: a946bd4e2a529e5fba9c9547d03d3f91806618a3)
- Drop unrequired for-upstream patches.
- BuildRequires and Requires new device-mapper version for udev sync support.

* Tue Oct 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4.9-9
- 0012-RH-explicitly-disable-dm-udev-sync-support-in-kpartx.patch

* Mon Oct 19 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4.9-8
- Split patches in "for-upstream" and "RH" series.
- Replace 0011-RH-multipathd-blacklist-all-by-default.patch with
  version from Benjamin Marzinski.
- Update udev rules 0010-RH-multipath-rules-udev-changes.patch.
- rpmlint cleanup:
  * Drop useless-provides kpartx.
  * Cleanup tab vs spaces usage.
  * Summary not capitalized.
  * Missing docs in libs package.
  * Fix init script LSB headers.
- Drop README* files from doc sections (they are empty).

* Thu Oct 15 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4.9-7
- Add patch 0010-RH-Set-friendly-defaults.patch:
  * set rcdir to fedora default.
  * do not install kpartx udev bits.
  * install redhat init script.
  * Cleanup spec file install target.
- Add patch 0011-RH-multipathd-blacklist-all-by-default.patch:
  * Fix BZ#528059
  * Stop installing default config in /etc and move it to the doc dir.

* Tue Oct 13 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4.9-6
- Updated to latest upstream 0.4.9 code : multipath-tools-091013.tar.gz
  (git commit id: aa0a885e1f19359c41b63151bfcface38ccca176)
- Drop, now upstream, patches:
  * fix_missed_uevs.patch.
  * log_all_messages.patch.
  * uninstall.patch.
  * select_lib.patch.
  * directio_message_cleanup.patch.
  * stop_warnings.patch.
- Drop redhatification.patch in favour of spec file hacks.
- Drop mpath_wait.patch: no longer required.
- Merge multipath_rules.patch and udev_change.patch.
- Rename all patches based on source.
- Add patch 0009-RH-fix-hp-sw-hardware-table-entries.patch to fix
  default entry for hp_sw and match current kernel.
- Add multipath.conf.redhat as source instead of patch.
- spec file:
  * divide runtime and build/setup bits.
  * update BuildRoot.
  * update install section to apply all the little hacks here and there,
    in favour of patches against upstream.
  * move ldconfig invokation to libs package where it belong.
  * fix libs package directory ownership and files.

* Thu Aug 20 2009 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.9-5
- Fixed problem where maps were being added and then removed.
- Changed the udev rules to fix some issues.

* Thu Jul 30 2009 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.9-4
- Fixed build issue on i686 machines.

* Wed Jul 29 2009 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.9-3
- Updated to latest upstream 0.4.9 code : multipath-tools-090729.tgz
  (git commit id: d678c139719d5631194b50e49f16ca97162ecd0f)
- moved multipath bindings file from /var/lib/multipath to /etc/multipath
- Fixed 354961, 432520

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 6 2009 Mike Snitzer <snitzer@redhat.com> - 0.4.9-1
- Updated to latest upstream 0.4.9 code: multipath-tools-090429.tgz
  (git commit id: 7395bcda3a218df2eab1617df54628af0dc3456e)
- split the multipath libs out to a device-mapper-multipath-libs package
- if appropriate, install multipath libs in /lib64 and /lib64/multipath

* Thu Apr 7 2009 Milan Broz <mbroz@redhat.com> - 0.4.8-10
- Fix insecure permissions on multipathd.sock (CVE-2009-0115)

* Fri Mar 6 2009 Milan Broz <mbroz@redhat.com> - 0.4.8-9
- Fix kpartx extended partition handling (475283)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 26 2008 Benjamin Marzinski <bmarzins@redhat.com> 0.4.8-7
- Since libaio is now in /lib, not /usr/lib, multipath no longer needs to
  statically link against it. Fixed an error with binding file and WWIDs
  that include spaces. Cleaned up the messages from the directio checker
  function.  Fixed the udev rules. Fixed a regression in multipath.conf
  parsing
- Fixed 457530, 457589

* Wed Aug 20 2008 Benjamin Marzinski <bmarzins@redhat.com> 0.4.8-6
- Updated to latest upstream 0.4.8 code: multipath-tools-080804.tgz
  (git commit id: eb87cbd0df8adf61d1c74c025f7326d833350f78)
- fixed 451817, 456397 (scsi_id_change.patch), 457530 (config_space_fix.patch)
  457589 (static_libaio.patch)

* Fri Jun 13 2008 Alasdair Kergon <agk@redhat.com> - 0.4.8-5
- Rebuild (rogue vendor tag). (451292)

* Mon May 19 2008 Benjamin Marzinksi <bmarzins@redhat.com> 0.4.8-4
- Fixed Makefile issues.

* Mon May 19 2008 Benjamin Marzinksi <bmarzins@redhat.com> 0.4.8-3
- Fixed ownership build error.

* Mon May 19 2008 Benjamin Marzinksi <bmarzins@redhat.com> 0.4.8-2
- Forgot to commit some patches.

* Mon May 19 2008 Benjamin Marzinski <bmarzins@redhat.com> 0.4.8-1
- Updated to latest Upstream 0.4.8 code: multipath-tools-080519.tgz
  (git commit id: 42704728855376d2f7da2de1967d7bc71bc54a2f)

* Tue May 06 2008 Alasdair Kergon <agk@redhat.com> - 0.4.7-15
- Remove unnecessary multipath & kpartx static binaries. (bz 234928)

* Fri Feb 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.7-14
- fix sparc64
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.7-13
- Autorebuild for GCC 4.3

* Wed Nov 14 2007 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.7-12
- Fixed the dist tag so building will work properly.

* Mon Feb 05 2007 Alasdair Kergon <agk@redhat.com> - 0.4.7-11.fc7
- Add build dependency on new device-mapper-devel package.
- Add dependency on device-mapper.

* Wed Jan 31 2007 Benjamin Marzinksi <bmarzins@redhat.com> - 0.4.7-10.fc7
- Update BuildRoot and PreReq lines.

* Mon Jan 15 2007 Benjamin Marzinksi <bmarzins@redhat.com> - 0.4.7-9.fc7
- Fixed spec file.

* Mon Jan 15 2007 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.7-8.fc7
- Update to latest code (t0_4_7_head2)

* Wed Dec 13 2006 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.7-7.fc7
- Update to latest code (t0_4_7_head1)

* Thu Sep  7 2006 Peter Jones <pjones@redhat.com> - 0.4.7-5
- Fix kpartx to handle with drives >2TB correctly.

* Thu Aug 31 2006 Peter Jones <pjones@redhat.com> - 0.4.7-4.1
- Split kpartx out into its own package so dmraid can use it without
  installing multipathd
- Fix a segfault in kpartx

* Mon Jul 17 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-4.0
- Updated to latest source. Fixes bug in default multipath.conf

* Wed Jul 12 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-3.1
- Added ncurses-devel to BuildRequires

* Wed Jul 12 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-3.0
- Updated to latest source. deals with change in libsysfs API

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.4.7-2.2.1
- rebuild

* Mon Jul 10 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-2.2
- fix tagging issue.

* Mon Jul 10 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-2.1
- changed BuildRequires from sysfsutils-devel to libsysfs-devel

* Wed Jun 28 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-2.0
- Updated to latest upstream source, fixes kpartx udev rule issue

* Mon Jun 06 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-1.0
- Updated to Christophe's latest source

* Mon May 22 2006 Alasdair Kergon <agk@redhat.com> - 0.4.5-16.0
- Newer upstream source (t0_4_5_post59).

* Mon May 22 2006 Alasdair Kergon <agk@redhat.com> - 0.4.5-12.3
- BuildRequires: libsepol-devel, readline-devel

* Mon Feb 27 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.5-12.2
- Prereq: chkconfig

* Mon Feb 20 2006 Karsten Hopp <karsten@redhat.de> 0.4.5-12.1
- BuildRequires: libselinux-devel

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.4.5-12.0.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Benjamin Marzinski <bmarzins@redhat.com> -0.4.5-12.0
- Updated to latest upstream source (t0_4_5_post56)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.4.5-9.1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Dec 19 2005 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.5-9.1
- added patch for fedora changes

* Fri Dec 16 2005 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.5-9.0
- Updated to latest upstream source (t)_4_5_post52)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sun Dec  4 2005 Peter Jones <pjones@redhat.com> - 0.4.4-2.6
- rebuild for newer libs

* Tue Nov 15 2005 Peter Jones <pjones@redhat.com> - 0.4.4-2.5
- unsplit kpartx.  parted knows how to do this now, so we don't
  need this in a separate package.

* Tue Nov 15 2005 Peter Jones <pjones@redhat.com> - 0.4.4-2.4
- split kpartx out into its own package

* Fri May 06 2005 Bill Nottingham <notting@redhat.com> - 0.4.4-2.3
- Fix last fix.

* Thu May 05 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-2.2
- Fix last fix.

* Wed May 04 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-2.1
- By default, disable the multipathd service.

* Tue Apr 19 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-2.0
- Fix core dump from last build.

* Tue Apr 19 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-1.0
- Move cache file into /var/cache/multipath.

* Fri Apr 08 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-0.pre8.1
- Remove pp_balance_units.

* Mon Apr 04 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-0.pre8.0
- Incorporate numerous upstream fixes.
- Update init script to distribution standards.

* Tue Mar 01 2005 Alasdair Kergon <agk@redhat.com> - 0.4.2-1.0
- Initial import based on Christophe Varoqui's spec file.
